# start here
class SaveSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, encoding='euc-kr')

    def filter_data_by_region(self, customer_address):
        try:
            filtered_df = self.df[self.df['관할구청'] == customer_address]

            if filtered_df.empty:
                print("잘못된 지역입니다. 다시 입력해주세요.")
                return []
            else:
                return filtered_df
        except KeyError:
            print("잘못된 지역입니다. 다시 입력해주세요.")
            return []

    def update_reviews(self, center_name, rating, review):
        if '리뷰갯수' not in self.df.columns:
            self.df['리뷰갯수'] = 0

        if '평균평점' not in self.df.columns:
            self.df['평균평점'] = 0.0

        if '리뷰' not in self.df.columns:
            self.df['리뷰'] = ''

        # 센터 찾기
        index = self.df[self.df['시설'] == center_name].index

        if not index.empty:
            index = index[0]

            # 기존 리뷰, 평균 평점 및 리뷰 지수 가져오기
            existing_reviews = self.df.at[index, '리뷰']
            average_rating = self.df.at[index, '평균평점']
            review_index = self.df.at[index, '리뷰갯수']

            # 새 리뷰를 기존 리뷰와 연결
            updated_review = f"{existing_reviews}\n{review_index + 1}. Rating: {rating}, Review: {review}" if existing_reviews else f"{review_index + 1}. Rating: {rating}, Review: {review}"

            # 리뷰,평점 업데이트
            if existing_reviews:
                total_ratings = average_rating * len(existing_reviews.split('\n')) + rating
                new_average_rating = total_ratings / (len(existing_reviews.split('\n')) + 1)
            else:
                new_average_rating = rating

            self.df.at[index, '평균평점'] = new_average_rating
            self.df.at[index, '리뷰'] = updated_review
            self.df.at[index, '리뷰갯수'] = review_index + 1

            # csv파일에 저장
            self.df.to_csv(self.file_path, index=False, encoding='euc-kr')

            print(f"{center_name}의 리뷰가 추가 되었습니다!")
        else:
            print(f"{center_name}을 찾을 수 없습니다.")
# end here
