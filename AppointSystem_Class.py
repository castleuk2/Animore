class AppointSystem:
    def __init__(self):
        while True:
            try:
                patient_info = input("환자의 이름, 나이, 종류, 증상을 쉼표로 구분하여 입력해주세요: ").split(',')
                if len(patient_info) == 4:
                    break 
                else:
                    print("잘못된 형식입니다. 다시 입력해주세요.")
            except Exception as e:
                print(f"에러 발생: {e}")

        self.name = patient_info[0]
        self.age = patient_info[1].strip()
        self.type = patient_info[2].strip()
        self.symptom = patient_info[3].strip()
        self.patient_info = [self.name, self.age, self.type, self.symptom]

    def request_appoint(self):
        while True:
            try:
                time = input("예약을 희망하는 월, 일, 시간을 구분하여 입력해주세요: ")
                self.time = time
                break
            except Exception as e:
                print(f"에러 발생: {e}")
