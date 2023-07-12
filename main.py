# Print my name
print("Alaric")

# Assign my favourite number to a variable
fav_num = 9
# Find my favourite number squared
fav_num_sq = fav_num * fav_num

# Create variable for a count up loop
count_up = 1

# Loop to count up to my favourite number squared
while (count_up <= fav_num_sq):
  print(count_up)
  count_up = count_up+1

# Create class engineers with fixed attribute skill 
class FixedEngineer:
  def __init__(self, skill):
    self.skill = "Problem Solver"

# Create class engineers which inherits the fixed attribute, along with individual attributes name, type and years of experience
class AllEngineer(FixedEngineer):
  def __init__(self, name , type , experience):
    super().__init__(self)
    self.name = name
    self.type = type
    self.experience = experience

  # Create function to request the attributes of each object within      the class
  def requestattributes(self):
    return self.skill , self.name , self.type , self.experience

# Create 2 different engineers
eng1 = AllEngineer("Bill", "Civil", 12)
eng2 = AllEngineer("Tim", "Electrical", 24)

# Print both engineers attributes
print(eng1.requestattributes())
print(eng2.requestattributes())