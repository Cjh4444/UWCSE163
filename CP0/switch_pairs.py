def switch_pairs(word):    
    return_string = ""
    for i in range(0, len(word) - 1, 2):
        return_string += word[i+1] + word[i]

    return_string += word[len(word) - 1] if len(word) % 2 == 1 else ""
    return return_string

def main():
    assert switch_pairs("example") == "xemalpe"
    assert switch_pairs("hello there") == "ehll ohtree"

if __name__ == "__main__":
    main()

    