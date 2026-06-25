#Calculating Costs
host_prov_pric=0.51
per_day_cost=host_prov_pric*24
print("Cost to operate one server per day: ",per_day_cost)
print("Cost to operate one server per week: ",per_day_cost*7)
print("Cost to operate one server per month: ",per_day_cost*30)
print("Total no. of days to operate one server with $918: ",918/per_day_cost)