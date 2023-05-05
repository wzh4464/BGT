def majority(votes):
    # return the median of votes
    if len(votes) == 0:
        return None
    else:
        return max(set(votes), key=votes.count)


class General:
    def __init__(self, id, traitor):
        self.id = id
        self.traitor = traitor
        self.value = None

    def OM(self, m, lieutenant_list, recieved_value):
        self.value = recieved_value
        message = []
        votes = []
        if self.traitor:
                # output traitor's id
                print("Traitor: ", self.id)
                for i in lieutenant_list:
                    # input each fake value
                    message.append(int(input("Vote to lieutenant " + str(i.id) + ": ")))
                    i.value = message[-1]
        else:
                # return all votes with self.value
                for i in lieutenant_list:
                    message.append(recieved_value)
                    i.value = message[-1]
        if m == 0:
            return message
        else:
            # votes[i] = majority of [OM(m-1, new_lieutenant_list), self.value]
            for lieutenant in lieutenant_list:
                new_lieutenant_list = lieutenant_list.copy()
                new_lieutenant_list.remove(lieutenant)
                votes.append(majority([lieutenant.value] + lieutenant.OM(m-1, new_lieutenant_list, lieutenant.value)))
            return votes



        
# define 7 generals
general_list = []
for i in range(7):
    general_list.append(General(i, False))

# general 0,6 is traitor
general_list[0].traitor = True
general_list[6].traitor = True

print(general_list[0].OM(2, general_list[1:], 1))
