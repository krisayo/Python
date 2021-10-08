def american_drama(place, job, *args, **kwargs):
    print("-- Oh, I am so far away from", place, "!")
    print("-- Damn, me too... What do you do for a living?")
    print("-- I am a ", job, ".")
    for arg in args:
        print(arg)
    print("-" * 50)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
    print("\n")


dic = {"dreamer": "William Blake", "pedestrian": "George Smith", "setting": "Birmingham"}
lst = ["-- Do you at least have a cigar, sir?", "-- Sure, help yourself."]
american_drama("Tokyo", "hobo", *lst, **dic)

dic = {"dreamer": "Lucy Lu", "pedestrian": "Jeremiah Caine", "setting": "Huntsville, Alabama"}
lst = ["-- Do you at least have a cigar, little one?", "-- Nah, I sure don\'t."]
american_drama("Naperville", "school girl", *lst, **dic)
