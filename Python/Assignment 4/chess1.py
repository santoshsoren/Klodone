
import chess as ch
board = ch.Board()


def chess(): 

    while True:
        piece = input("Enter piece: ")
        move = input("Enter move: ")
        piece = ch.Move.from_uci(move)
        bool = piece in board.legal_moves
        if bool == True:
            board.push(piece)
            print(board)
            if board.is_checkmate() == True:
                print("check mate...!!!  GAME OVER")
                break
            elif board.is_stalemate() == True:
                print("Stalemate...!!!  GAME OVER")
                braek
            elif board.is_insufficient_material() == True:
                print("Game Drawn by insufficient material...!!!  GAME OVER")
                break
            elif board.is_check() == True:
                print("Check...!!!")

            ch.Move.null
            
        else:
            print("Illegal move...!!!")
        
    
    
chess()
