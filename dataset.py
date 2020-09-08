# importing pandas for the csv/xlsx reading
# I've been playing around with pandas quite a bit
import pandas as pd

# voting_data = pd.read_excel(
#     r"C:\Users\KT\Documents\School\OCC\CS 131\2015electionresultspyithu.xlsx"
# )
# voting_data_subset = pd.DataFrame(voting_data, columns=["party_name"])
# print(voting_data_subset)

# I commented that out because I wanted to see how the .dataframe would work for me


# 1. subset of data as strings
# first 16 x 7 cells

voting_data_as_strings = """pcode_ts	pcode_st	name_st	name_ts	candidate_name	votes	party_name
MMR001001	MMR001	Kachin	Myitkyina	U Sai Sein Own	2041	Shan Nationalities Democratic Party
MMR001001	MMR001	Kachin	Myitkyina	U Win Tin	640	The Union of Myanmar Federation of National Politics
MMR001001	MMR001	Kachin	Myitkyina	U Naw Taung	2605	National Unity Party
MMR001001	MMR001	Kachin	Myitkyina	U Nyunt Win	26800	Union Solidarity and Development Party
MMR001001	MMR001	Kachin	Myitkyina	Daw Bauk Jar (or)  Lwann Nge	2788	National Democratic Force
MMR001001	MMR001	Kachin	Myitkyina	U In Htone Khar Naw Sam	48961	National League for Democracy
MMR001001	MMR001	Kachin	Myitkyina	U Hlaing Myint U	3653	Tai-Leng Nationalities Development Party
MMR001001	MMR001	Kachin	Myitkyina	U Bayan Lee	6910	Kachin State Democracy Party
MMR001001	MMR001	Kachin	Myitkyina	U Htwal Naw	1937	The Kachin National Congress for Democracy
MMR001001	MMR001	Kachin	Myitkyina	U Kyan Lay	4236	Lisu National Development Party
MMR001001	MMR001	Kachin	Myitkyina	U Larein (or) U Phaw Myar Larein	3860	Kachin Democratic Party
MMR001001	MMR001	Kachin	Myitkyina	U La Zatt Lwann Kaung	1210	Lhaovo National Unity and Development Party
MMR001002	MMR001	Kachin	Waingmaw	Daw Aye Huai  (or)  Yin Yin Aye	1993	Shan Nationalities Democratic Party
MMR001002	MMR001	Kachin	Waingmaw	U Khaw Tarr	3974	National Unity Party
MMR001002	MMR001	Kachin	Waingmaw	U Kyaw Kyaw Aung	8485	Union Solidarity and Development Party
"""
print(voting_data_as_strings)

# 2 subset of data as tuples

voting_data_as_tuples = pd.read_excel(
    r"C:\Users\KT\Documents\School\OCC\CS 131\2015electionresultspyithu.xlsx"
)
# fancy way to do it I found on stackexchange but it seemed as though the following does the trick, albeit in a much less fashionable manner:
# [(a) for a, row in voting_data_as_tuples.iterrows()]
# print(voting_data_as_tuples)
for row in voting_data_as_tuples.iterrows():
    print(
        row
    )  # I have to learn how to prevent everything from being printed. Something to limit the for loop but my Java experience did not come handy here.

# 3 custom class
class Voting:
    def __init__(
        self,
        postalcode_township,
        postalcode_state,
        name_state,
        name_township,
        candidate_name,
        number_of_votes,
        party_name,
    ):
        self.pcode_ts = postalcode_township
        self.pcode_st = postalcode_state
        self.name_st = name_state
        self.name_ts = name_township
        self.candidate_name = candidate_name
        self.votes = number_of_votes
        self.party_name = party_name

    def name_of_candidate(self):
        print("Name of Candidate: " + self.candidate_name)

    def party_affiliation(self):
        print("Affiliation: " + self.party_name)

    def votes_received(self):
        print("Number of votes received: " + self.votes)


test1 = Voting(
    "MMR001001",
    "MMR001",
    "Kachin",
    "Myitkyina",
    "U Sai Sein Own",
    "2041",
    "Shan Nationalities Democratic Party",
)
test1.name_of_candidate()
test1.party_affiliation()
test1.votes_received()
