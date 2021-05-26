
environment_types = [
    { "name": "Arctic" },
    { "name": "Coastal" },
    { "name": "Desert" },
    { "name": "Forest" },
    { "name": "Grassland" },
    { "name": "Hill" },
    { "name": "Jungle" },
    { "name": "Mountain" },
    { "name": "Swamp" },
    { "name": "Underdark" },
    { "name": "Underwater" },
    { "name": "Urban" },
]

organization_types = [
    { "name": "Business" },
    { "name": "Magical" },
    { "name": "Natural" },
    { "name": "Religious" },
    { "name": "Other Interest" },
    { "name": "Ethical" },
    { "name": "Criminal" },
    { "name": "Political" },
]

person_types = [
    { "name": "Business" },
    { "name": "Magical" },
    { "name": "Natural" },
    { "name": "Religious" },
    { "name": "Other Interest" },
    { "name": "Ethical" },
    { "name": "Criminal" },
    { "name": "Political" },
    { "name": "Independent" },
]

person_type_reasons = [
    { "person_type": "Business", "reasoning": "Born into a family business." }
]

arcane_locations = [
    { 
        "name": "Hermit Hut", 
        "description": "A single hut inhabited by a very old hermit. 'Ah, I’ve been expecting you for so long! I’m glad you could make it!' The hermit offers them a fortune reading and insists they stay the night. When the party leaves, they find the hut and hermit aren’t there anymore.",
        "related_people": [ 
            { "min_roll": 1, "max_roll": 1, "quantity": "1d1", "person_type": "Magician" } 
        ],
        "related_organizations": [ 
            { "min_roll":  1, "max_roll": 4, "quantity": "0d1", "organization_type": "" }, 
            { "min_roll":  5, "max_roll": 8, "quantity": "1d1", "organization_type": [ "Magical" ] }, 
            { "min_roll":  9, "max_roll": 9, "quantity": "1d2", "organization_type": [ "Magical", "Business" ] }, 
        ],
    },
    { 
        "name": "Giant Stone Monkey Head", 
        "description": "A single hut inhabited by a very old hermit. 'Ah, I’ve been expecting you for so long! I’m glad you could make it!' The hermit offers them a fortune reading and insists they stay the night. When the party leaves, they find the hut and hermit aren’t there anymore.",
        "related_people": [ 
            { "min_roll": 1, "max_roll": 1, "quantity": "1d1", "person_type": "Magician" } 
        ],
        "related_organizations": [ 
            { "min_roll":  1, "max_roll": 4, "quantity": "0d1", "organization_type": "" }, 
            { "min_roll":  5, "max_roll": 8, "quantity": "1d1", "organization_type": [ "Magical" ] }, 
            { "min_roll":  9, "max_roll": 9, "quantity": "1d2", "organization_type": [ "Magical", "Business" ] }, 
        ],
    }

]

