import glob
import os
import json

reports_dir = 'G:/ben_reports/ben_reports'

# Duyệt qua tất cả các tệp tin trong thư mục và các thư mục con
for filepath in glob.iglob(os.path.join(reports_dir, '**'), recursive=True):
    # Kiểm tra xem đường dẫn là một tệp tin và tồn tại
    if os.path.isfile(filepath):
        try:
            # Mở và đọc nội dung của tệp tin JSON
            with open(filepath, 'r') as f:
                data = json.load(f)
                
            # Trích xuất thông tin từ tệp tin JSON
            name = data.get('target', {}).get('file', {}).get('name')
            if name is not None:
                print(name)

                # Kiểm tra và xử lý dữ liệu 'apistats' nếu có
                behavior_data = data.get('behavior', {})
                if 'apistats' in behavior_data:
                    apistats = {}
                    for apistat in behavior_data['apistats'].values():
                        apistats.update(apistat)
                    
                    # Tạo đối tượng JSON mới để lưu trữ thông tin
                    savejson = {'name': name, 'apistats': apistats, 'class': 'malware'}
                    
                    # Xây dựng đường dẫn đến thư mục lưu trữ
                    save_dir = 'F:\gan_nhan_test'
                    if not os.path.exists(save_dir):
                        os.makedirs(save_dir)
                    
                    # Xây dựng đường dẫn đến tệp tin mới
                    savepath = os.path.join(save_dir, name[:-3] + 'json')
                    
                    # Ghi đối tượng JSON mới vào tệp tin
                    with open(savepath, 'w') as s:
                        json.dump(savejson, s, ensure_ascii=False)
        except json.JSONDecodeError:
            print(f"Error reading JSON file: {filepath}")
