def recommend_fertilizer(n, p, k):

    if n < 50:
        return "Nitrogen Deficiency. Apply Urea."

    elif p < 30:
        return "Phosphorus Deficiency. Apply DAP."

    elif k < 30:
        return "Potassium Deficiency. Apply MOP."

    else:
        return "NPK levels are balanced."


if __name__ == "__main__":
    result = recommend_fertilizer(40, 60, 70)
    print(result)