from faker import Faker

myfake = Faker()

# Farker의 메소드를 통해서 어떤 종류의 가짜데이터를 뽑아낼지 결정할 수 있음
# myfake.함수 이름 
# Seed 파일 (코드를 실행할때 같은 faker 파일 표출)
myfake.seed(1)

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())

