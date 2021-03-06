import random

michigan_facts = [
        "The name Michigan is the French form of the Ojibwa word mishigamaa, meaning 'large water' or 'large lake'.",
        "Alpena, MI is the home of the world's largest cement plant.",
        "Rogers City, MI boasts the world's largest limestone quarry.",
        "Elsie, MI is the home of the world's largest registered Holstein dairy herd.",
        "Michigan is first in the United States production of peat and magnesium compounds and second in gypsum and iron ore.",
        "Colon, MI is home to the world's largest manufacturer of magic supplies.",
        "The state Capitol with its majestic dome was built in Lansing in 1879.",
        "Although Michigan is often called the 'Wolverine State' there are no longer any wolverines in Michigan.",
        "Michigan ranks first in state boat registrations.",
        "The Packard Motor Car Company in Detroit manufactured the first air-conditioned car in 1939.",
        "The oldest county in Michigan (based on date of incorporation) is Wayne in 1815.",
        "Sault Ste. Marie was founded by Father Jacques Marquette in 1668. It is the third oldest remaining settlement in the United States.",
        "In 1817 the University of Michigan was the first university established by any of the states. Originally named Cathelepistemian and located in Detroit the name was changed in 1821. The university moved to Ann Arbor in 1841.",
        "The city of Novi was named from its designation as Stagecoach Stop # 6 or No.VI.",
        "Michigan State University has the largest single campus student body of any Michigan university. It is the largest institution of higher learning in the state and one of the largest universities in the country.",
        "Michigan State University was founded in 1855 as the nation's first land-grant university and served as the prototype for 69 land-grant institutions later established under the Morrill Act of 1862. It was the first institution of higher learning in the nation to teach scientific agriculture.",
        "The largest village in Michigan is Caro.",
        "The Petoskey stone is Michigan's official state stone. It is a rock and a fossil, often pebble-shaped, that is composed of a fossilized coral, Hexagonaria percarinata.",
        "The Mackinac Bridge is one of the longest suspension bridges in the world. Connecting the upper and lower peninsulas of Michigan, it spans 5 miles over the Straits of Mackinac, which is where Lake Michigan and Lake Huron meet. The Mighty Mac took 3 years to complete and was opened to traffic in 1957.",
        "Gerald R. Ford grew up in Grand Rapids and became the 38th president of the United States. He attended the University of Michigan where he was a football star. He served on a World War II aircraft carrier and afterward represented Michigan in Congress for 24 years. He was also was an Eagle Scout, the highest rank in Boy Scouts.",
        "The Kellogg Company has made Battle Creek the Cereal Capital of the World. The Kellogg brothers accidentally discovered the process for producing flaked cereal products and sparked the beginning of the dry cereal industry.",
        "The painted turtle is Michigan's state reptile.",
        "The western shore of Michigan has many sand dunes. The Sleeping Bear Dunes rise 460 feet above Lake Michigan. Living among the dunes is the dwarf lake iris the official state wildflower.",
        "Vernors ginger ale was created in Detroit and became the first soda pop made in the United States. In 1862, pharmacist James Vernor was trying to create a new beverage when he was called away to serve our country in the Civil War. When he returned, 4 years later, the drink he had stored in an oak case had acquired a delicious gingery flavor.",
        "The Detroit Zoo was the first zoo in America to feature cageless, open-exhibits that allowed the animals more freedom to roam.",
        "Michigan is the only place in the world with a floating post office. The J.W. Westcott II is the only boat in the world that delivers mail to ships while they are still underway. They have been operating for 125 years.",
        "Michigan was admitted to the Union in 1837, the 26th state.",
        "Michigan has the longest freshwater shoreline in the world, 3,126 miles.",
        "Michigan has more than 11,000 inland lakes and more than 36,000 miles of streams.",
        "The State motto is 'Si quaeris peninsulam amoenam circumspice.' (If you seek a pleasant peninsula, look about you.)",
        "Michigan has 116 lighthouses and navigational lights.",
        "Forty of the state's 83 counties adjoin at least one of the Great Lakes.",
        "Michigan is the only state that touches four of the five Great Lakes.",
        "Standing anywhere in the state a person is within 85 miles of one of the Great Lakes.",
        "Michigan includes 56,954 square miles of land area; 1,194 square miles of inland waters; and 38,575 square miles of Great Lakes water area.",
        "Sault Ste. Marie was established in 1668 making it the oldest town between the Alleghenies and the Rockies.",
        "Michigan was the first state to provide in its Constitution for the establishment of public libraries.",
        "Michigan was the first state to guarantee every child the right to tax-paid high school education.",
        "Four flags have flown over Michigan - French, English, Spanish and United States.",
        "Isle Royal Park shelters one of the largest moose herds remaining in the United States.",
        "Some of the longest bulk freight carriers in the world operate on the Great Lakes. Ore carriers 1,000 feet long sail Michigan's inland seas.",
        "The Upper Michigan Copper Country is the largest commercial deposit of native copper in the world.",
        "The 19 chandeliers in the Capitol in Lansing are one of a kind and designed especially for the building by Tiffany's of New York. Weighing between 800-900 pounds apiece they are composed of copper, iron and pewter.",
        "The first auto traffic tunnel built between two nations was the mile-long Detroit-Windsor tunnel under the Detroit River.",
        "The nation's first regularly scheduled air passage service began operation between Grand Rapids and Detroit in 1926.",
        "In 1879 Detroit telephone customers were first in the nation to be assigned phone numbers to facilitate handling calls.",
        "In 1929, the Michigan State Police established the first state police radio system in the world.",
        "Grand Rapids is home to the 24-foot Leonardo da Vinci horse, called Il Gavallo, it is the largest equestrian bronze sculpture in the Western Hemisphere.",
        "Michigan has 19,000,000 acres of forest cover"
]

def run(data, settings):
    if (data['payload'] == 'michigan fact') or (data['payload'] == 'Michigan fact'):
        return random.choice(michigan_facts)
