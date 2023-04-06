import warnings

import matplotlib.pyplot as plt


def goodie(csv):
    with open(csv, "r") as f:
        txt = f.read()
        f.close()
    lines = txt.splitlines()
    lines = [l.replace(",good,", "") for l in lines if "good" in l]
    return lines


def cap_a(sample_str="abc, it's easy as one, two, three."):
    "Capitalises any lower case 'a' in a string"
    return sample_str.replace("a", "A")


def cap_b(sample_str="abc, it's easy as one, two, three."):
    "Capitalises any lower case 'b' in a string"
    return sample_str.replace("b", "B")


def cap_abc(sample_str="abc, it's easy as one, two, three."):
    "Capitalise any occurence of A, B or C"
    s = cap_a(sample_str)
    s = cap_b(s)
    return s.replace("c", "C")


def fruity_bars(
        fruits=['apple', 'blueberry', 'cherry', 'orange'],
        counts=[40, 100, 30, 55]
        ):
    """Generate the example fruit bar chart from matplotlib docs"""
    fig, ax = plt.subplots()

    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    return plt
