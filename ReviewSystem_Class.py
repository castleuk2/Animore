# start here
class ReviewSystem:
    def __init__(self, center_list, file_path):
        self.centers = {center[0]: {'address': center[1], 'phone': center[2], 'reviews': []} for center in
                        center_list}
        self.file_path = file_path

    def add_review(self, center_name, rating, review):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            reviews.append({'평점': rating, '리뷰': review})

            # csv파일 업데이트 새로운 데이터로
            save_system = SaveSystem(self.file_path)
            save_system.update_reviews(center_name, rating, review)
            print(f"{center_name}의 리뷰가 추가 되었습니다!")         
         
    def write_review_interaction(self,center_list):
        while True:
            center_name = input("리뷰를 작성하시겠습니까? 다녀온 병원 이름을 입력하세요. (나가기: 'exit'): ")
                
            if center_name.lower() == 'exit':
                return
                
            # 병원이 있는지 확인
            if center_name in [center[0] for center in center_list]:
                break                    
            elif center_name not in [center[0] for center in center_list]:
                continue
        
        while True:
            try:
                rating_input = input("평점을 매겨주세요. (0, 1, 2, 3, 4, 5) (나가기: 'exit'): ")
                
                if rating_input.lower() == 'exit':
                    return  

                rating = int(rating_input)
                if 0 <= rating <= 5:
                    break
                                
                else:
                    print("0 부터 5 사이의 정수만 입력 가능합니다. 다시 입력해주세요.")
            except ValueError:
                print("0 부터 5 사이의 정수만 입력 가능합니다. 다시 입력해주세요.")
              
        while True:
            review = input("리뷰를 작성해주세요. (나가기: 'exit') : ")
            if review.lower() == 'exit':
                return
            
            elif review.strip():
                break
            
            else:
                print("리뷰란을 비워둘 수 없습니다. 다시 입력해주세요.")
        
        self.add_review(center_name, rating, review)
# end here
