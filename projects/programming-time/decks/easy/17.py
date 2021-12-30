# λ (lambda) calculus
# "Most computer languages (like C
# and C++ or Java) are invented, λ
# calculus is discovered."
#     -- Phillip Wadler
# This example is a snippet from
# gist.github.com/gcr/848437
TRUE  = lambda t: lambda f: t()
FALSE = lambda t: lambda f: f()
IF =                              \
   lambda cond:                   \
     lambda t:                    \
     lambda f:                    \
       cond(lambda: t)(lambda: f)
AND =                             \
  lambda a:                       \
    lambda b:                     \
      IF(a)(b)(FALSE)
OR =                              \
  lambda a:                       \
    lambda b:                     \
      IF(a)(TRUE)(b)

print(IF                          \
      (AND                        \
         (OR                      \
            (TRUE)                \
            (FALSE))              \
         (TRUE))                  \
      (lambda: ⚂)                 \
      (lambda: ⚂)())
