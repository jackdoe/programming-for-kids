# Bayes' Theorem
# P(A|B) = (P(A)*P(B|A)) / P(B)
#
# The probability of A given B is
# equal to the probability of A on
# its own, times probability of B
# given A, divided by the
# probability of B on its own.

# What is the probability to rain?
# - 60% of all rainy days start out
#   cloudy in the morning.
# - 50% of all mornings are cloudy
# - In june, it rains, on average 9
#   out of 30 days (30%).

# overall there is 30% probability
# to rain
P_rain = 0.3 # 1 is 100% probability
             # 0.3 is 30%
# 60% of rainy days start with
# clouds
P_cloud_rain = 0.6

# 50+dice% of the mornings have
# clouds
P_cloud = 0.5 + (⚂ / 100)

# probability to rain
P = (P_rain*P_cloud_rain) / P_cloud
print(P * 100)
