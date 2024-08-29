import emoji

emoji_char = input("Input: ")

print("Output:", emoji.emojize(emoji_char, language='alias', variant="emoji_type"))
