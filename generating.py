from itertools import permutations
import json

# Define fixed locations for breakfast, lunch, dinner, and check-in hotel
fixed_locations = [
    {"Event": "Breakfast", "Place": "Pak Mat Western Cafe", "Remarks": "Kickstart your day at Pak Mat Western Cafe, where a hearty breakfast awaits. This cozy spot offers a delightful mix of Western flavors, setting the perfect tone for a day of exploration in Penang.", "Link": "https://maps.app.goo.gl/CQL1DLg7X4shKgqJ7"},
    {"Event": "Lunch", "Place": "BM Famous Ban Chien Kueh", "Remarks": "Elevenses at BM Famous Ban Chien Kueh is a must! Indulge in the delightful taste of this local favorite, a perfect mid-morning treat that captures the essence of Penang's culinary traditions.", "Link": "https://maps.app.goo.gl/kTBVVoMQKaL92Gjz7"},
    {"Event": "Dinner", "Place": "Queensbay Mall", "Remarks": "Queensbay Mall is not just a shopping destination; it's a complete experience. Enjoy a delicious dinner and indulge in some retail therapy, surrounded by a vibrant atmosphere and a plethora of choices.", "Link": "https://maps.app.goo.gl/idTHc6p8gqW2AiTaA"},
    {"Event": "Check in hotel", "Place": "Tropicana 218 Macalister", "Remarks": "Experience comfort and style at Tropicana 218 Macalister. Your home away from home, this hotel provides a welcoming retreat, ensuring a relaxing stay in the heart of Penang.", "Link": "https://maps.app.goo.gl/Mi3tnvAdj62bJXvL9"}
]

# Generate all permutations for the remaining events
remaining_events = [
    {"Event": "Elevenses", "Place": "Aki Pancake", "Remarks": "Elevenses take a delightful turn at Aki Pancake. Indulge in a variety of fluffy pancakes with a twist, making it a perfect spot to satisfy your mid-morning cravings.", "Link": "https://maps.app.goo.gl/M8qxkWgBsvZnitRG9"},
    {"Event": "Attractions", "Place": "Mengkuang Dam", "Remarks": "Discover the tranquility of nature at Mengkuang Dam. The serene surroundings and picturesque landscapes make it an ideal destination for those seeking a peaceful escape and scenic beauty.", "Link": "https://maps.app.goo.gl/E3w4QwVDAqQTxT2EA"},
    {"Event": "Attractions", "Place": "Pantai Seagate View Pulau Jerjak", "Remarks": "Explore the breathtaking views at Pantai Seagate on Pulau Jerjak. This hidden gem offers a unique perspective of Penang's coastal beauty, making it a must-visit destination for nature enthusiasts.", "Link": "https://maps.app.goo.gl/a9n8aBvHB3ezAARZ6"},
    {"Event": "Dessert", "Place": "Bingsu Monster", "Remarks": "Satisfy your sweet cravings at Bingsu Monster. This dessert haven offers a cool and refreshing escape with its delightful array of Bingsu creations, a perfect way to beat the Penang heat.", "Link": "https://maps.app.goo.gl/PZB6RouxCKmrxi15A"}
]

# Ensure that there are at least 5 remaining events for permutation
assert len(remaining_events) >= 4

# Generate all permutations for the remaining events
all_permutations = permutations(remaining_events, 4)  # Select 5 remaining events for permutation

# User and system messages
user_message = {"role": "user", "content": "country: Malaysia, state: Penang, day: 1"}
system_message = {"role": "system", "content": "Jeff is a suggestive chatbot that is good at giving tourist ideas."}

# Print the permutations in the desired format
for idx, permutation in enumerate(all_permutations, 1):
    day_events = fixed_locations.copy()
    day_events.insert(2, permutation[0])  # Insert first remaining event after breakfast
    day_events.insert(4, permutation[1])  # Insert second remaining event after lunch
    day_events.insert(6, permutation[2])  # Insert third remaining event after dinner
    day_events.insert(8, permutation[3])  # Insert fourth remaining event after dessert

    events_content = " ".join([f"{{Event: {event['Event']}, Place: {event['Place']}, Remarks: {event['Remarks']}, Link: {event['Link']}}}" for event in day_events])
    
    assistant_message = {
        "role": "assistant",
        "content": f"Day 1: {events_content}"
    }

    # Output the messages
    print(json.dumps({"messages": [system_message, user_message, assistant_message]}, indent=4))
    print("\n")
