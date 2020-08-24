sentence = ' xoxo love xoxo   '

# Leading whitepsace are removed
print(sentence.strip())  # xoxo love xoxo 

print(sentence.strip(' xoe'))  #lov 为什么?

# Argument doesn't contain space
# No characters are removed.
print(sentence.strip('sti'))  # xoxo love xoxo 

sentence = 'android is awesome'
print(sentence.strip('an'))  # droid is awesome
