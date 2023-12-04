class ReviewSystem:
    def __init__(self, center_list):
        self.centers = {center[0]: {'address': center[1], 'phone': center[2], 'reviews': []} for center in center_list}
  
    def add_review(self, center_list, center_name, rating, review):
        if center_name in self.centers:
            reviews = self.centers[center_name]['reviews']
            reviews.append({'평점': rating, '리뷰': review})

            # Calculate the updated average rating
            total_ratings = sum(review['평점'] for review in reviews)
            average_rating = total_ratings / len(reviews)

            # Update the center's average rating
            self.centers[center_name]['average_rating'] = average_rating

            # Update the center_list with the new reviews
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
        else:
            print(f"{center_name} 병원 리스트에서 해당 병원을 찾을 수 없습니다2.")

    def write_review_interaction(self,center_list):
        center_name = input("\n리뷰를 작성하시겠습니까? 다녀온 병원 이름을 입력하세요. (나가기: 'exit'): ")
        if center_name.lower() == 'exit':
            return

        rating = int(input("평점을 매겨주세요. (0-5): "))
        review = input("리뷰를 작성해주세요. : ")
        self.add_review( center_list, center_name, rating, review)
