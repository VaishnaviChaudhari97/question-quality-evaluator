from textblob import TextBlob


def get_cognitive(file):
    lostag = file.split('\n')
    lostag = list(filter(None, lostag))
    lostag = [name for name in lostag if name.strip()]

    recall = ["state", "choose", "define", "how", "label", "list", "match", "name", "omit", "recall", "relate",
              "select", "show", "spell", "tell", "what", "when", "where", "which", "who", "why"]
    understand = ["classify", "contrast", "describe", "demonstrate", "discuss", "explain", "extend", "illustrate",
                  "infer", "interpret", "outline", "relate", "rephrase", "show", "summarize", "translate", "understand"]
    apply = ["application", "apply", "append", "build", "choose", "construct", "create", "delete",
             "develop", "display", "experiment with", "identify", "implement", "insert", "interview", "print",
             "merge", "organize", "plan", "perform", "program", "select", "solve", "sort", "traverse", "use", "utilize",
             "find", "calculate", "write"]
    analyze = ["analyze", "assume", "categorize", "check", "classify", "compare", "conclusion", "contrast", "discover",
               "dissect", "distinguish", "divide", "determine", "differentiate", "examine", "inference", "inspect",
               "motive", "relationships", "simplify", "survey", "theme"]
    evaluate = ["agree", "appraise", "assess", "award", "choose", "conclude", "criteria", "criticize", "decide",
                "deduct", "defend", "disprove", "estimate", "evaluate", "importance", "influence", "interpret", "judge",
                "justify", "mark", "measure", "opinion", "perceive", "prioritize", "prove", "rate", "recommend",
                "select", "support", "suggest"]
    create = ["adapt", "model", "build", "combine", "compile", "compose", "design", "develop", "elaborate", "estimate",
              "formulate", "happen", "imagine", "improve", "invent", "maximize", "minimize", "original", "originate",
              "plan", "predict", "propose", "solution", "test", "theory", "maximize"]

    def cog_level(temp_list):
        lev = ""
        if set(temp_list) & set(recall):
            lev = "Recall"
        if set(temp_list) & set(understand):
            lev = "Understand"
        if set(temp_list) & set(apply):
            lev = "Apply"
        if set(temp_list) & set(analyze):
            lev = "Analyze"
        if set(temp_list) & set(evaluate):
            lev = "Evaluate"
        if set(temp_list) & set(create):
            lev = "Create"
        return (lev)

    lo_cg = []
    id = 1

    for lo in lostag:
        elem = {}
        d = lo.split()
        p = cog_level(d)
        elem["id"] = id
        elem["cognitive"] = p
        id = id+1
        lo_cg.append(elem)
    return(lo_cg)


def get_concepts(file):
    blob = file.split("\n")
    blob = list(filter(None, blob))
    blob = [name for name in blob if name.strip()]

    b = []  # los in a list
    for lo in blob:
        b.append(lo)

    def concept_extr(temp):
        temp1=TextBlob(temp)
        sample = []
        for i in range(5):
            for ngram in temp1.ngrams(i):
                 sample.append(" ".join(ngram))
                 sample.append(" ".join(ngram.lemmatize()))
            sample = list(dict.fromkeys(sample))
        return (sample)

    lo_co = []
    id = 1

    for los in b:
        elem = {}
        x = concept_extr(los)
        elem["id"] = id
        elem["concepts"] = x
        id = id+1
        lo_co.append(elem)

    return(lo_co)