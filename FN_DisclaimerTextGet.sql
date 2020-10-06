CREATE OR REPLACE FUNCTION dbo."FN_DisclaimerTextGet"(
    IN  pi_DisclaimerId         INTEGER,
    IN  pi_DisclaimerTextTypeId INTEGER
)
    RETURNS TABLE
    (
        "CustomerID"          INTEGER,
        "ParentResellerId"    INTEGER,
        "DisclaimerId"        INTEGER
        "Level"               INTEGER,
        "CustomTextContentId" UUID,
        "ForUseByChildren"    SMALLINT,
        "State"               INTEGER,
        "CustomTextTypeId"    INTEGER,
        "CustomTextId"        UUID
    )
    LANGUAGE plpgsql
AS
$BODY$
-- ========================================================================================================
-- Description : 
--             :
-- Author      : 
-- --------------------------------------------------------------------------------------------------------
-- [Change History]
-- --------------------------------------------------------------------------------------------------------
-- Date (yyyy-mm-dd)  Changed By                 Build               Etrack/Jira     Change Description
--
-- 2020-06-08          Jayaprakash(k1)           20_02_RobsonDB                      Migrated from SQL Server
-- ========================================================================================================
-- ------------------------------------------------------------------------------------------------------------
-- [COPYIGHT NOTICE]
-- ------------------------------------------------------------------------------------------------------------
-- Copyright © 2020 Broadcom. All rights reserved.
-- The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries.
--
-- This software and all information contained therein is confidential and proprietary and shall not be
-- duplicated, used, disclosed or disseminated in any way except as authorized by the applicable license agreement,
-- without the express written permission of Broadcom. All authorized reproductions must be marked with this language.
--
-- EXCEPT AS SET FORTH IN THE APPLICABLE LICENSE AGREEMENT, TO THE EXTENT PERMITTED BY APPLICABLE LAW OR
-- AS AGREED BY BROADCOM IN ITS APPLICABLE LICENSE AGREEMENT, BROADCOM PROVIDES THIS DOCUMENTATION “AS IS”
-- WITHOUT WARRANTY OF ANY KIND, INCLUDING WITHOUT LIMITATION, ANY IMPLIED WARRANTIES OF MERCHANTABILITY,
-- FITNESS FOR A PARTICULAR PURPOSE, OR NONINFRINGEMENT. IN NO EVENT WILL BROADCOM BE LIABLE TO THE END USER OR
-- ANY THIRD PARTY FOR ANY LOSS OR DAMAGE, DIRECT OR INDIRECT, FROM THE USE OF THIS DOCUMENTATION,
-- INCLUDING WITHOUT LIMITATION, LOST PROFITS, LOST INVESTMENT, BUSINESS INTERRUPTION, GOODWILL, OR LOST DATA,
-- EVEN IF BROADCOM IS EXPRESSLY ADVISED IN ADVANCE OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE
-- ========================================================================================================

-- note this function only works for default disclaimers
-- this function is only called by up_insight_DisclaimerTextGet (and the initial disclaimers migration script)
DECLARE
    v_Count               INTEGER;
    v_MaxCount            INTEGER;
    v_CustomTextContentId UUID;

BEGIN
     
     CREATE TEMPORARY TABLE IF NOT EXISTS tt_Result
     (
         "CustomerID"          INTEGER,
         "ParentResellerId"    INTEGER,
         "DisclaimerId"        INTEGER,
         "Level"               INTEGER,
         "CustomTextContentId" UUID,
         "ForUseByChildren"    SMALLINT,
         "State"               INTEGER,
         "CustomTextTypeId"    INTEGER,
         "CustomTextId"        UUID
     );
    -- insert inheritance hierarchy
     WITH RECURSIVE cte AS    
     (
                     SELECT c."CustomerID",
                            c."ParentResellerId",
                            d."DisclaimerId",
                            0 "Level"
                       FROM dbo."Customers" c
                       JOIN dbo."Disclaimer" d
                         ON d."CustomerId" = c."CustomerID"
                        AND d."isDefault" = 1
                        AND d."DisclaimerId" = pi_DisclaimerId
                  UNION ALL
                     SELECT c."CustomerID",
                            c."ParentResellerId",
                            d."DisclaimerId",
                            "Level" + 1
                       FROM dbo."Customers" c
                       JOIN dbo."Disclaimer" d
                         ON d."CustomerId" = c."CustomerID"
                        AND d."DisclaimerName" = 'Default'
                       JOIN cte
                         ON cte."ParentResellerId" = c."CustomerID"
                      WHERE cte."CustomerID" <> dbo.FN_RootCustomer()
                        AND c."DateDeleted" = '9999-12-31 23:59:59'
                )
                INSERT INTO tt_Result
                (
                            "CustomerID",
                            "ParentResellerId",
                            "DisclaimerId",
                            "Level",
                            "CustomTextTypeId",
                            "ForUseByChildren"
                )       
                     SELECT "CustomerID",
                            "ParentResellerId",
                            "DisclaimerId",
                            ROW_NUMBER() OVER (ORDER BY "Level" DESC),
                            pi_DisclaimerTextTypeId,
                            1
                       FROM cte;
                                
	-- insert initial customer level default disclaimer record
                INSERT INTO tt_Result
                (
                            "CustomerID",
                            "ParentResellerId",
                            "DisclaimerId",
                            "Level",
                            "CustomTextTypeId",
                            "ForUseByChildren"
                )       
                    SELECT  c."CustomerID",
                            c."ParentResellerId",
                            d."DisclaimerId",
                    (SELECT MAX("Level") FROM tt_Result) + 1 AS "Level",
                            pi_DisclaimerTextTypeId,
                            0
                       FROM dbo."Customers" c 
                 INNER JOIN dbo."Disclaimer" d 
                         ON d."CustomerId" = c."CustomerID"
                      WHERE "DisclaimerId" = pi_DisclaimerId;

                     SELECT MAX("Level") 
                       INTO v_MaxCount
                       FROM tt_Result;

    v_Count := 1;            
    WHILE v_Count <= v_MaxCount
        LOOP           
            UPDATE tt_Result r1
               SET "CustomTextContentId" = cth."CustomTextContentId",
                   "State" = cth."State",
                   "CustomTextId" = cth."CustomTextId"
              FROM dbo."CustomTextHierarchy" cth 
             WHERE cth."ownerid" = r1."DisclaimerId"
               AND cth."ownertypeid" = 3
               AND cth."CustomTextTypeId" = r1."CustomTextTypeId"
               AND cth."ForUseByChildren" = r1."ForUseByChildren"
               AND r1."Level" = v_Count;     
               v_Count := v_Count + 1;
        END LOOP;
    RETURN QUERY(
        SELECT * FROM tt_Result
    );
END;
$BODY$
