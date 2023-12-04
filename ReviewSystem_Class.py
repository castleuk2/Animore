class ReviewSystem:
    def __init__(self, center_list):
        self.centers = {center[0]: {'address': center[1], 'phone': center[2], 'reviews': []} for center in center_list}
  
    def add_review(self, center_list, center_name, rating, review):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            reviews.append({'평점': rating, '리뷰': review})

            # 업데이트된 평균 평점 계산
            total_ratings = sum(review['평점'] for review in reviews)
            average_rating = total_ratings / len(reviews)

            # 센터의 평균 등급 업데이트
            self.centers[center_name]['average_rating'] = average_rating

            # 새로운 리뷰로 center_list 업데이트
            for center in center_list:
               if center[0] == center_name:
                if len(center) >= 6:
                    center[4] = average_rating
                    center[5] = reviews
                else:
                    center.extend([average_rating, reviews])
                break

            print(f"{center_name}의 리뷰가 추가 되었습니다!")
            print(center_list)
       

    def write_review_interaction(self,center_list):
        while True:
            center_name = input("리뷰를 작성하시겠습니까? 다녀온 병원 이름을 입력하세요. (나가기: 'exit'): ")
            if center_name.lower() == 'exit':
                return
                    
            # 병원이 있는지 확인
            if center_name not in [center[0] for center in center_list]:
                print(f"{center_name}이란 병원을 리스트에서 찾을 수 없습니다. 다시 입력해주세요.")
                continue
            
            while True:
                try:
                    rating = int(input("평점을 매겨주세요. (0, 1, 2, 3, 4, 5): "))
                    if 0 <= rating <= 5:
                        break
                    else:
                        print("0 부터 5 사이의 정수만 입력 가능합니다. 다시 입력해주세요.")
                except ValueError:
                    print("0 부터 5 사이의 정수만 입력 가능합니다. 다시 입력해주세요.")
                  
            while True:
                review = input("리뷰를 작성해주세요. : ")
                if review.strip():
                    break
                else:
                    print("리뷰란을 비워둘 수 없습니다. 다시 입력해주세요.")
            
            self.add_review( center_list, center_name, rating, review)
