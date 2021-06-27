from replit import clear
#HINT: You can call clear() to clear the output in the console.

auction_pool = {}
end_of_bids = False

def find_highest_bidder():
  pass


while not end_of_bids:
  
  name = input("Please insert your name: ")
  bid = input("Please insert your bid: ")
  auction_pool[name] = bid
  more_players = input('Are there more players? (y/n): ') 
  
  if more_players == 'y':
    clear()
  elif more_players == 'n': 
    end_of_bids = True




  





    
    
