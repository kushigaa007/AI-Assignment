print("Computers Knows the Following data")
print("a.	I am a human being")
print("b.	I am good")
print("c.	Good graders study well")
print("d.	Humans love graders")
print("e.	Every human does not study well")

concerned_Data=("Every","Human","good grader","study well")

print("Query : Is every human good grader")

knowledge=[{"study well":False,"good grader":False,"human":True,"every":True},{"study well":True,"good grader":True,"human":True,"every":False},
           {"study well":False,"good grader":False,"human":True,"every":True},{"study well":False,"good grader":False,"human":False,"every":False}]
p = not(knowledge[0]["human"] and knowledge[0]["every"]) or knowledge[0]["good grader"]
a=1
for i in range(len(knowledge)):
    q = not(knowledge[i]["human"] and knowledge[i]["every"]) or knowledge[i]["good grader"]
    if ( p == q ):
        continue
    else:
        print("No")
        a=0
        break;
if(a==1):
    print("Yes")
