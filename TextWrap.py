import textwrap 

value = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

def wrap(string, max_width):
    txt = []
    # Wrap this text. 
    wrapper = textwrap.TextWrapper(width=max_width) 
    
    word_list = wrapper.wrap(text=string) 
    
    # Print each line. 
    for element in word_list: 
        #print(element)
        txt.append(element)
    return '\n'.join(txt)
    
result = wrap(value, max_width)
print result
