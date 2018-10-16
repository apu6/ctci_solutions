def urlify(s, length):
    arr_s = list(s)
    for i in range(0, length):
        if arr_s[i] == " ":
            arr_s[i+3:] = arr_s[i+1:-2]
            arr_s[i:i+3] = "%20"
    result = ''.join(arr_s)
    return result


if __name__ == "__main__":
  print(urlify("Mr John Smith    ",13))