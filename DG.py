def deaf_grandma(grandma, counter = 0) :

    print(grandma)
    kid = input()

    if kid == '' :
      return deaf_grandma('WHAT?!')
    elif any(i.islower() for i in kid) :
      return deaf_grandma('SPEAK UP KID!')
    elif kid == 'GOODBYE!' and counter == 1 :
      print('LATER, SKATER!', end='')
    elif kid == 'GOODBYE!' :
      return deaf_grandma('LEAVING SO SOON?', counter = 1)
    elif any(i.isupper() for i in kid) :
      return deaf_grandma('NO, NOT SINCE 1946!')

print(deaf_grandma('HEY KID!')) 