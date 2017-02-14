import random
from random import shuffle
import time

A = 11
H2 = 2
H3 = 3
H4 = 4 
H5 = 5 
H6 = 6 
H7 = 7 
H8 = 8 
H9 = 9 
H10 = 10
HJ = 10
HQ = 10
HK = 10

S2 = 2
S3 = 3
S4 = 4 
S5 = 5 
S6 = 6 
S7 = 7 
S8 = 8 
S9 = 9 
S10 = 10
SJ = 10
SQ = 10
SK = 10


C2 = 2
C3 = 3
C4 = 4 
C5 = 5 
C6 = 6 
C7 = 7 
C8 = 8 
C9 = 9 
C10 = 10
CJ = 10
CQ = 10
CK = 10

D2 = 2
D3 = 3
D4 = 4 
D5 = 5 
D6 = 6 
D7 = 7 
D8 = 8 
D9 = 9 
D10 = 10
DJ = 10
DQ = 10
DK = 10



# defines deck as an array of all the cards above
deck = [H2, H3, H4, H5, H6 ,H7, H8, H9, H10, HJ ,HQ ,HK ,
S2 ,S3 ,S4 ,S5 ,S6 ,S7 ,S8 ,S9 ,S10 ,SJ ,SQ ,SK ,
C2 ,C3 ,C4 ,C5 ,C6 ,C7 ,C8 ,C9 ,C10 ,CJ ,CQ ,CK, 
D2 ,D3 ,D4 ,D5 ,D6 ,D7 ,D8 ,D9 ,D10, DJ ,DQ ,DK, A, A, A, A]





shuffle(deck)# shuffle the deck to random the index



#creates a function to evaulate value of ace
def total(hand):
	#assigns total an int of the hand passed in
	total = sum(hand)

	#returns the number of times aces will occur in the hand
	ACES = hand.count(A)
	
	#creates an if statement to determind value of ace
	if total > 21 and ACES > 0:
		while ACES > 0 and total > 21:
			total = total - 10 # the value of total goes down by 10
			ACES = ACES - 1 # aces minus by one

	# returns total to user		
	return total 


"""game logic below"""
def game():
	player_in = True
	#keeping track of score
	player_wins = 0
	house_wins = 0

	while player_in:

	
		player_hand = [deck.pop(), deck.pop()]
		player_Bust = False

		while player_in:
			total_player_points = total(player_hand)
			print "The player has been dealt %s with a value of %d" % (player_hand, total_player_points)
			time.sleep(1)
			
			if total_player_points > 21:
				print "Player busts"
				player_Bust = True
				break

			elif total_player_points == 21:
				print "Black Jack"
				break

			else:
				call_stay = raw_input("Hit or Stay?: ").lower()
				
				if "hit" in call_stay:
					player_hand.append(random.choice(deck))
					time.sleep(1)

				else:
					break

		#loop will keep going
		while player_in:
			house_bust = False
			house_hand = [deck.pop(), deck.pop()]
			#loop will keep going until house loses or user stops
			while True:
				total_points_house = total(house_hand)
				house_sentence = "The House draws %s with a value of %d" %(house_hand, total_points_house)
				time.sleep(1)

				if total_points_house < 18:
					print house_sentence
					house_hand.append(random.choice(deck))
					time.sleep(1)
				else:
					break

			if total_points_house > 21:
				print house_sentence
				print "House Busts"
				#break the loop
				house_bust = True
				# condition false to know that player also did not bust
				if player_Bust == False:
					print "Player Wins"
					player_wins = player_wins + 1

			elif total_points_house > total_player_points:
				house_wins = house_wins + 1
				print house_sentence
				print "House Wins, Player Loses"

			elif total_points_house == total_player_points:
				print house_sentence
				print "Draw"

			elif total_player_points > total_points_house:

				if player_Bust == False:
					print "Player Wins, House Loses"
					player_wins = player_wins + 1
				
				elif house_bust == False:
					house_wins = house_wins + 1
					print "House Wins"
			break
		print "Player = %d  House = %d" % (player_wins, house_wins)

		ex = raw_input("Press Enter to play again, q to quit: ").lower()
		if 'q' in ex:
			break

game()
























































