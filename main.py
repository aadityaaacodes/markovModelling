para = "The sun dipped below the horizon, casting a warm golden glow over the quiet town. Birds began to settle in the trees, their evening songs blending with the gentle rustling of leaves. In the distance, the sound of laughter echoed from the park where children were chasing fireflies, their tiny lights blinking in the dusk. People leisurely walked along the cobbled streets, pausing to chat with familiar faces. The world seemed to slow down, as if time itself was taking a deep breath before the night fully embraced the days final moments."
para2 = ""

# remove special chars
for letter in para:
    if (letter.isalpha() or letter == ' '):
        para2 += letter

para2.split(" ")

# assign a matrix
mat1 = {}

