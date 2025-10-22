
"""
straight - consecutive cards, symbol length = 5/no dupes
flush - suite length = 1
straight flush - both straight and flush
royal flush - straight flush + AKQJT
four of a kind - symbol length = 2, symbol count = 4
three of a kind - symbol count = 3
"""


symbol_to_value = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}


def seperate_hands(hands_str:str) -> tuple[list[str],list[str]]:
    hand1 = []
    hand2 = []
    temp = hands_str.replace(" ","")
    start_point = len(temp)//2
    for i in range(0,start_point,2):
        hand1.append(temp[i:i+2])
        hand2.append(temp[start_point+i:start_point+i+2])
    #print(hand1,hand2)
    return hand1,hand2
    #return [hands_list[2*i:2*i+2] for i in range(len(hands_list)//4)],[hands_list[2*i+10:2*i+12] for i in range(len(hands_list)//4)]

def evaluate_hand(hand:list[str]) -> str:
    symbol_count = {}
    suite_count = {}
    
    for card in hand:
        symbol,suite = card[0],card[1]
        symbol_count = counter(symbol,symbol_count)
        suite_count = counter(suite,suite_count)
   
    duplicates = check_duplicates(symbol_count)        
    if duplicates:
        three_kind = False
        three_kind_value = 0
        pair = False
        pair_value = 0
        for symbol,count in symbol_count.items():
            symbol_value = symbol_to_value[symbol]
            if count == 4:
                return f"Four Of A Kind,{symbol}"
            elif count == 3:
                three_kind = True
                three_kind_value = symbol_value
            elif count == 2:
                if pair:
                    return f"Two Pair,{max(pair_value,symbol_value)}"
                else:
                    pair = True
                    pair_value = symbol_value
        
        if pair and three_kind:
            return f"Full House,{three_kind_value}"
        elif pair:
            return f"One Pair,{pair_value}"
        elif three_kind:
            return f"Three Of A Kind,{three_kind_value}"
            
    else:
        straight = check_consecutive_cards(hand)
        flush = check_flush(suite_count)
        if straight and flush:
            if equate_lists(symbol_count.keys(),["A","K","Q","J","T"]):
                return f"Royal Flush,{max([symbol_to_value[card[0]] for card in hand])}"
            return f"Straight Flush,{max([symbol_to_value[card[0]] for card in hand])}"
        elif straight:
            return f"Straight,{max([symbol_to_value[card[0]] for card in hand])}"
        elif flush:
            return f"Flush,{max([symbol_to_value[card[0]] for card in hand])}"
        
    return f"High Card,{max([symbol_to_value[card[0]] for card in hand])}"
        
        
def counter(key:str,dictionary:dict[str,int]) -> dict[str,int]:   
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1
    return dictionary

def equate_lists(list1:list,list2:list):
    for item in list1:
        if item not in list2:
            return False
    return True

def check_duplicates(symbol_count):
    if len(symbol_count) != 5:
        return True
    return False

def check_flush(suite_count:dict):
    if len(suite_count) == 1:
        return True
    return False

def check_consecutive_cards(hand:list[str]):
    max_chain_length = 4
    symbol_value_list = []
    ace = False
    smallest_value = largest_value = 0
    
    for card in hand:
        symbol = card[0]
        symbol_value = symbol_to_value[symbol]
        
        # if symbol == "A":
        #     ace = True
        # else:
        if not symbol_value_list:
            smallest_value = largest_value = symbol_value
        if smallest_value + max_chain_length >= symbol_value >= largest_value - max_chain_length:
            symbol_value_list.append(symbol_value)
            
            if symbol_value < smallest_value:
                smallest_value = symbol_value
            elif symbol_value > largest_value:
                largest_value = symbol_value
                
        else:
            return False

    # if ace:
    #     if not (smallest_value + max_chain_length == 14 or largest_value - max_chain_length == 1):
    #         return False
    
    return True
            
def retrieve_hands():
    with open("Euler 51-100\Euler 51-60\Euler54.txt","r") as file:
        for hands in file:
            yield seperate_hands(hands)
    
def get_next_high_card(hand:list[str],used_card:int):
    print(hand)
    value_list = [symbol_to_value[card[0]] for card in hand]
    return max([value for value in value_list if value != used_card])
        
def compare_hands(p1, p2, value1, value2, used1, used2):
    if value1 > value2:
        return True
    elif value1 == value2:
        if int(used1) > int(used2):
            return True
        elif int(used1) == int(used2):
            # Compare remaining cards in descending order
            values1 = sorted([symbol_to_value[card[0]] for card in p1], reverse=True)
            values2 = sorted([symbol_to_value[card[0]] for card in p2], reverse=True)
            for v1, v2 in zip(values1, values2):
                if v1 > v2:
                    return True
                elif v1 < v2:
                    return False
    return False

def main() -> None:
    hand_value = {
        "High Card":1,
        "One Pair":2,
        "Two Pair":3,
        "Three Of A Kind":4,
        "Straight":5,
        "Flush":6,
        "Full House":7,
        "Four Of A Kind":8,
        "Straight Flush":9,
        "Royal Flush":10   
    }
    
    count = 0
    
    for p1,p2 in retrieve_hands():
        data1 = evaluate_hand(p1)
        hand1 = data1.split(",")[0]
        value1 = hand_value[hand1]
        used1 = data1.split(",")[1]
        
        data2 = evaluate_hand(p2)
        hand2 = data2.split(",")[0]
        value2 = hand_value[hand2]
        used2 = data2.split(",")[1]
            
        if compare_hands(p1,p2,value1,value2,used1,used2):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
    # hand = ["AD","KD","QD","JD","TD"]
    # print(check_consecutive_cards(hand))

#     print(p1,p2)
    
