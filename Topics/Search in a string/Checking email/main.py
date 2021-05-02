def check_email(string):
    return all(["@" in string, " " not in string,
                "@." not in string, "." in string[string.find("@"):]])
