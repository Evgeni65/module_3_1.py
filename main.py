calls = 0
def count_calls():
    global  calls
    calls = calls + 1
def string_info(string):
       count_calls()
       a =  (len(string),(string.upper()),(string.lower()))
       print(a)
def  is_contains(string,list_to_search):
    count_calls()
    list_to_search = [s.lower() for s in list_to_search]
    print(string.lower() in list_to_search)
string_info('Abrakodabra')
string_info('Trindez')
is_contains('Urban',['urbaNs','Banah','uRbaN'])
is_contains('Namber',['naMbers','mamber','Novmber'])
print(calls)