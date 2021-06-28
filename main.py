from replit import clear
#HINT: You can call clear() to clear the output in the console.

auction_pool = {}
end_of_bids = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f'the winner is {winner}, with a bid of {highest_bid}')
    


from art import logo


print(logo)
while not end_of_bids:
  
  name = input("Please insert your name: ")
  bid = input("Please insert your bid: ")
  auction_pool[name] = int(bid)
  more_players = input('Are there more players? (y/n): ') 
  
  if more_players == 'y':
    clear()
  elif more_players == 'n': 
    find_highest_bidder(auction_pool)


    end_of_bids = True





 

'''
    highest_bidder = max(auction_pool.items(), key=operator.itemgetter(1))[0]
    print(f'The winner of the auction is {highest_bidder} with a bid of {auction_pool[highest_bidder]}')
    '''



    
    
