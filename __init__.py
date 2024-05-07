'''
def animateMove(move, screen, board, clock):
    """
    Animating a move
    """
    global colors
    d_row = move.end_row - move.start_row
    d_col = move.end_col - move.start_col
    frames_per_square = 10  # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square
    for frame in range(frame_count + 1):
        row, col = (move.start_row + d_row * frame / frame_count, move.start_col + d_col * frame / frame_count)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        color = colors[(move.end_row + move.end_col) % 2]
        end_square = p.Rect(move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw captured piece onto rectangle
        if move.piece_captured != '--':
            if move.is_enpassant_move:
                enpassant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_col * SQUARE_SIZE, enpassant_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            screen.blit(IMAGES[move.piece_captured], end_square)
        # draw moving piece
        screen.blit(IMAGES[move.piece_moved], p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        p.display.flip()
        clock.tick(60)
        
def makeMove(self, move):
        """
        Takes a Move as a parameter and executes it.
        (this will not work for castling, pawn promotion and en-passant)
        """
        self.board[move.start_row, move.start_col] = "--"
        self.board[move.end_row, move.end_col] = move.piece_moved
        self.move_log.append(move)  # log the move so we can undo it later
        self.white_to_move = not self.white_to_move  # switch players
        # update king's location if moved
        if move.piece_moved == "wK":
            self.white_king_location = (move.end_row, move.end_col)
        elif move.piece_moved == "bK":
            self.black_king_location = (move.end_row, move.end_col)

        # pawn promotion
        if move.is_pawn_promotion:
            # if not is_AI:
            #    promoted_piece = input("Promote to Q, R, B, or N:") #take this to UI later
            #    self.board[move.end_row][move.end_col] = move.piece_moved[0] + promoted_piece
            # else:
            self.board[move.end_row][move.end_col] = move.piece_moved[0] + "Q"

        # enpassant move
        if move.is_enpassant_move:
            self.board[move.start_row][move.end_col] = "--"  # capturing the pawn

        # update enpassant_possible variable
        if move.piece_moved[1] == "p" and abs(move.start_row - move.end_row) == 2:  # only on 2 square pawn advance
            self.enpassant_possible = ((move.start_row + move.end_row) // 2, move.start_col)
        else:
            self.enpassant_possible = ()

        # castle move
        if move.is_castle_move:
            if move.end_col - move.start_col == 2:  # king-side castle move
                self.board[move.end_row][move.end_col - 1] = self.board[move.end_row][
                    move.end_col + 1]  # moves the rook to its new square
                self.board[move.end_row][move.end_col + 1] = '--'  # erase old rook
            else:  # queen-side castle move
                self.board[move.end_row][move.end_col + 1] = self.board[move.end_row][
                    move.end_col - 2]  # moves the rook to its new square
                self.board[move.end_row][move.end_col - 2] = '--'  # erase old rook

        self.enpassant_possible_log.append(self.enpassant_possible)

        # update castling rights - whenever it is a rook or king move
        self.updateCastleRights(move)
        self.castle_rights_log.append(CastleRights(self.current_castling_rights.wks, self.current_castling_rights.bks,
                                                   self.current_castling_rights.wqs, self.current_castling_rights.bqs))

# Replace findBesetMove to get best move from stockfish
def findBestMove(game_state, valid_moves):
    #import stockfish as chess engine here 
    
    
    # Draw evaluation score# Draw evaluation score with a smaller font size
    font = p.font.SysFont(None, 18)  # Smaller font size to fit within the designated area
    score_text = f"Eval:\n{evaluation / 100:.2f}"  # Shorter text
    text_obj = font.render(score_text, True, p.Color('white'))

    # Adjust the position of the text to ensure it fits
    text_rect = text_obj.get_rect()
    text_rect.center = (BOARD_WIDTH + EVAL_BAR_WIDTH // 2, 10)  # Centered horizontally
    screen.blit(text_obj, text_rect)

    # Calculate the height for the white advantage bar
    if evaluation >= 0:  
        # Convert the evaluation score to a proportional height
        bar_height = (evaluation + 32000) / 64000 * evaluation_bar_height
        bar_rect = p.Rect(BOARD_WIDTH, evaluation_bar_height - bar_height, evaluation_bar_width, bar_height)
        bar_color = (0, 255, 0)  # Green for White's advantage
        p.draw.rect(screen, bar_color, bar_rect)
    else:  # If Black has the advantage, the green bar is smaller, emphasizing more gray
        # Proportional height when Black has an advantage (inverted)
        bar_height = (32000 - abs(evaluation)) / 64000 * evaluation_bar_height
        # Draw the reduced green bar for Black's advantage
        bar_rect = p.Rect(BOARD_WIDTH, evaluation_bar_height - bar_height, evaluation_bar_width, bar_height)
        p.draw.rect(screen, (0, 255, 0), bar_rect)
    
'''