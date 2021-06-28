from replit import clear
#HINT: You can call clear() to clear the output in the console.

auction_pool = {}
end_of_bids = False


from art import logo
import operator

print(logo)
while not end_of_bids:
  
  name = input("Please insert your name: ")
  bid = input("Please insert your bid: ")
  auction_pool[name] = bid
  more_players = input('Are there more players? (y/n): ') 
  
  if more_players == 'y':
    clear()
  elif more_players == 'n': 
    highest_bidder = max(auction_pool.items(), key=operator.itemgetter(1))[0]
    print(f'The winner of the auction is {highest_bidder} with a bid of {auction_pool[highest_bidder]}')

    end_of_bids = True





 





    
    
