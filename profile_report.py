import tkinter as tk
from tkinter import simpledialog
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from tkinter import messagebox
import sys
import os


def resource_path(relative_path):
    """Lấy đường dẫn tài nguyên từ PyInstaller"""
    try:
        # Khi đóng gói bằng PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Khi chạy từ mã nguồn
        base_path = os.path.dirname(os.path.realpath(__file__))
    
    full_path = os.path.join(base_path, relative_path)
    print(f"Đường dẫn tài nguyên: {full_path}")  # In ra đường dẫn để kiểm tra
    return full_path

# logo_path = resource_path("logo.jpeg")
# chart_path = resource_path("chartmg.jpeg")
# channel_path = resource_path("channel.jpeg")
logo_path= "D:/python/print_profile/logo.jpeg"
chart_path= "D:/python/print_profile/chartmg.jpeg"
channel_path= "D:/python/print_profile/channel.jpeg"

# Hàm đọc dữ liệu từ file config_line_X.txt
def read_config_line(file_path):
    # Kiểm tra nếu ứng dụng đang chạy dưới dạng .exe
    if getattr(sys, 'frozen', False):
        # Lấy đường dẫn tạm thời khi đóng gói thành .exe
        base_path = sys._MEIPASS
    else:
        # Đường dẫn thư mục gốc khi phát triển
        base_path = os.path.dirname(os.path.realpath(__file__))

    # Xây dựng đường dẫn đến thư mục config
    config_folder = os.path.join(base_path, 'config')
    
    # Tạo đường dẫn đầy đủ đến file config
    full_path = os.path.join(config_folder, file_path)
    
    # Đọc dữ liệu từ file
    with open(full_path, 'r') as file:
        data = file.readlines()
        
    # Chia nhỏ dữ liệu theo dấu chấm phẩy
    parsed_data = [line.strip().split(';') for line in data]
    
    return parsed_data

# Hàm tạo báo cáo với số lượng cột tùy chỉnh
def create_report(output_filename, logo_path, chart_path, channel_path, num_columns, line_data,model_name):
    # Lấy thư mục chứa chương trình hiện tại
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Đường dẫn đến thư mục report (nếu chưa tồn tại, tạo mới)
    report_dir = os.path.join(current_dir, 'report')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # Đảm bảo rằng tên file báo cáo là đầy đủ (bao gồm cả đường dẫn)
    output_path = os.path.join(report_dir, output_filename)

    # Đặt trang giấy A4 nằm ngang
    c = canvas.Canvas(output_path, pagesize=landscape(A4))

    # Chèn tiêu đề báo cáo
    title_x = 250
    title_y = 565
    c.setFont("Times-Roman", 24)
    c.drawString(title_x, title_y, "Temperature Analysis Report")

    # Vị trí cho logo
    logo_x = 700
    logo_y = 500
    logo_width = 100
    logo_height = 45
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(0.5)
    c.rect(675, 245, 160, 310)
    c.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)

    # khung detail:
    detail_width = 155
    detail_height = 15
    detail_x = 677
    detail_y = logo_y - 15
    c.setLineWidth(0.5)
    c.rect(detail_x, detail_y, detail_width, detail_height)
    detail_text_x = detail_x + 2
    detail_text_y = detail_y + 4
    c.setFont("Times-Roman",9)
    c.drawString(detail_text_x,detail_text_y, "Details:")
    # Khung infor
    infor_width = detail_width
    infor_height = 150
    infor_x = detail_x
    infor_y = detail_y - infor_height - 3
    c.setLineWidth(0.5)
    c.rect(infor_x, infor_y, infor_width, infor_height)
    # text infor:
    company_txt_x = infor_x + 2
    company_txt_y = infor_y + infor_height - 10
    c.drawString(company_txt_x, company_txt_y, f'{str(line_data[4][0])}')
    #########
    FileName_txt_x = infor_x + 2
    FileName_txt_y = company_txt_y - 10
    c.drawString(FileName_txt_x, FileName_txt_y, f"File Name: {model_name} ")
    #########
    oven_txt_x = infor_x + 2
    oven_txt_y = FileName_txt_y - 10
    c.drawString(oven_txt_x, oven_txt_y, f'Oven:  {str(line_data[5][1])}')
    #########
    testDate_txt_x = infor_x + 2
    testDate_txt_y = oven_txt_y - 10
    c.drawString(testDate_txt_x, testDate_txt_y, f'{str(line_data[6][0])}')
    #########
    printDate_txt_x = infor_x + 2
    printDate_txt_y = testDate_txt_y - 10
    c.drawString(printDate_txt_x, printDate_txt_y, f'{str(line_data[7][0])}')
    # Khung remark:
    rm_width = detail_width
    rm_height = 80
    rm_x = detail_x
    rm_y = infor_y - rm_height - 3
    c.setLineWidth(0.5)
    c.rect(rm_x, rm_y, rm_width, rm_height)
    rm_text_x = rm_x +2
    rm_text_y = rm_y + rm_height - 8
    c.drawString(rm_text_x, rm_text_y, "Remark:")
    # khung chữ ký
    sign_x = detail_x - 50
    sign_y = 25
    c.setFont("Times-Roman",11)
    c.drawString(sign_x,sign_y,"EN__________                  IPQC__________")


    # Vị trí cho biểu đồ (Chart)
    chart_x = 20
    chart_y = 250  # Đặt biểu đồ dưới phần dữ liệu
    chart_width = 650
    chart_height = 300

    # Vẽ khung bao quanh biểu đồ
    c.rect(chart_x - 5, chart_y - 5, chart_width + 10, chart_height + 10)  # Khung cho biểu đồ

    # Chèn biểu đồ vào báo cáo
    c.drawImage(chart_path, chart_x, chart_y, width=chart_width, height=chart_height)

    # Chèn Oven 
    Oven_stove_x = 25 # Vị trí chữ 
    Oven_stove_y = chart_y-20  # Vị trí chữ 

    # Vẽ chữ 
    c.setFont("Times-Roman", 11)
    c.drawString(Oven_stove_x, Oven_stove_y, f"Oven stove: {str(line_data[5][1])}")
    # Chèn Oven & speed)conveyor
    Oven_speed_x = Oven_stove_x + 150 # Vị trí chữ 
    Oven_speed_y = chart_y-20  # Vị trí chữ 

    # Vẽ chữ 
    c.setFont("Times-Roman", 11)
    c.drawString(Oven_speed_x, Oven_speed_y, f"Speed: {str(line_data[3][1])}  CM/Min ")

    # Thêm khung zone
    zone_width = 45  
    zone_height = 15  
    zone_x = 20 
    zone_y = Oven_speed_y-20  
    c.rect(zone_x, zone_y, zone_width, zone_height)
    
    tempZone_x = zone_x + 1  # Vị trí chữ  bên trong khung
    tempZone_y = zone_y + 2  # Vị trí chữ  theo chiều dọc

    # Vẽ chữ "TemperatureZone"
    c.setFont("Times-Roman", 9)
    c.drawString(tempZone_x, tempZone_y, "Temp.Zone")

    # #####Thêm khung aboveZone
    aboveZone_width = 45  
    aboveZone_height = 15  
    aboveZone_x = 20 
    aboveZone_y = Oven_speed_y-20 - zone_height 
    c.rect(aboveZone_x, aboveZone_y, aboveZone_width, aboveZone_height)
    
    textInSide_x = aboveZone_x + 1  # Vị trí chữ  bên trong khung
    textInSide_y = aboveZone_y + 2  # Vị trí chữ  theo chiều dọc

    # Vẽ chữ "AboveZone"
    c.setFont("Times-Roman", 9)
    c.drawString(textInSide_x, textInSide_y, "AboveZone")

    # ######Thêm khung belowZone
    belowZone_width = 45  
    belowZone_height = 15  
    belowZone_x = 20 
    belowZone_y = Oven_speed_y-20 - zone_height - aboveZone_height 
    c.rect(belowZone_x, belowZone_y, belowZone_width, belowZone_height)
    
    textInSide_x = belowZone_x + 1  # Vị trí chữ  bên trong khung
    textInSide_y = belowZone_y + 2  # Vị trí chữ  theo chiều dọc

    # Vẽ chữ "belowZone"
    c.setFont("Times-Roman", 9)
    c.drawString(textInSide_x, textInSide_y, "BelowZone")

    # Vẽ bảng dưới phần "Oven stove"
    table_x = aboveZone_width + 20  # Vị trí bắt đầu bảng
    table_y = Oven_speed_y-20  # Khoảng cách từ chữ "Oven stove" tới bảng

    cell_width = 25  # Chiều rộng mỗi ô
    cell_height = 15  # Chiều cao mỗi ô
    # vẽ channel
    channel_width = 820
    channel_height = 120
    channel_x = 15
    channel_y  = belowZone_y - channel_height - 10 
    c.drawImage(channel_path,channel_x, channel_y, channel_width, channel_height)
    

    # Vẽ các dòng ngang và dọc của bảng
    for row in range(3):  # 3 dòng (header, above, below)
        for col in range(num_columns):  # Duyệt qua tất cả các cột
            x = table_x + col * cell_width
            y = table_y - row * cell_height
            c.rect(x, y, cell_width, cell_height)
            
            # Nếu là dòng đầu tiên (header), vẽ tên cột
            if row == 0:
                c.setFont("Times-Roman", 9)
                if col < len(line_data[0]):
                    # print(line_data[0])
                    c.drawString(x + 5, y + 4, str(line_data[0][col]))  # Vẽ tên cột trong header
                
            # Vẽ dữ liệu từ dòng above vào bảng
            if row == 1:  # Dòng thứ 2 là dòng dữ liệu "above"
                c.setFont("Times-Roman", 9)
                if col < len(line_data[1]):
                    c.drawString(x + 5, y + 4, str(line_data[1][col]))  # Vẽ dữ liệu của dòng "above"
            
            # Vẽ dữ liệu từ dòng below vào bảng
            if row == 2:  # Dòng thứ 3 là dòng dữ liệu "below"
                c.setFont("Times-Roman", 9)
                if col < len(line_data[2]):
                    c.drawString(x + 5, y + 4, str(line_data[2][col]))  # Vẽ dữ liệu của dòng "below"


    # Lưu báo cáo
    c.save()

# Hàm tạo GUI để nhập số cột và chọn dòng
def create_gui():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Tạo report pdf")

    # Label và Entry để nhập số lượng cột
    label_zone_number = tk.Label(root, text="Nhập số lượng Oven zone:")
    label_zone_number.pack(pady=10)

    column_entry = tk.Entry(root)
    column_entry.pack(pady=10)
    # Nhập mã hàng
    label_model = tk.Label(root, text= "Mã hàng:")
    label_model.pack(pady=10)
    model_entry = tk.Entry(root)
    model_entry.pack(padx=10)

    # tạo radiobutton để tùy chọn line:
    var = tk.StringVar()
    #cac tùy chọn cho radiobutton_line
    def on_select():
        var.get()
    var.set("config_line_1.txt")
    # tạo các radionbutton_other line
    radio_line_1 = tk.Radiobutton(root, text="Line_1",variable=var, value="config_line_1.txt", command=on_select)
    radio_line_1.pack()
    radio_line_2 = tk.Radiobutton(root, text="Line_2",variable=var, value="config_line_2.txt",command=on_select)
    radio_line_2.pack()
    radio_line_3 = tk.Radiobutton(root, text="Line_3",variable=var, value="config_line_3.txt",command=on_select)
    radio_line_3.pack()
    radio_line_4 = tk.Radiobutton(root, text="Line_4",variable=var, value="config_line_4.txt",command=on_select)
    radio_line_4.pack()

    # Nút để tạo báo cáo
    def on_button_click():
        try:
            num_columns = int(column_entry.get())  # Lấy số cột từ người dùng
            if num_columns < 1:
                messagebox.showerror(title="error!",message="Lỗi nhập liệu, Số lượng cột phải lớn hơn 0.")
                return
            model_name = str(model_entry.get())
            if not model_name:
                messagebox.showerror(title="error!",message="Chưa nhập tên mã hàng.")
                return
            
            # Lấy giá trị tùy chọn được chọn từ radiobutton_line
            selected_line = var.get()  # Ví dụ: "config_line_1.txt"
            
            # Đọc dữ liệu từ file config_line_x.txt
            line_data = read_config_line(selected_line)
            
            # Kiểm tra nếu line_data không hợp lệ hoặc rỗng:
            if not line_data:
                messagebox.showerror(title="error!",message=f"Lỗi dữ liệu, không có dữ liệu hợp lệ trong file: {selected_line}")

            # Tạo báo cáo PDF với dữ liệu từ file và số cột người dùng nhập
            create_report(f'{model_name}.pdf', logo_path,chart_path, channel_path, num_columns, line_data, model_name)
            
            messagebox.showinfo(title="Success", message="Đã tạo báo cáo thành công!")

        except ValueError as e:
            messagebox.showerror(title="Error", message=f"Đã xảy ra lỗi: {e}")

    # Nút để tạo báo cáo
    button = tk.Button(root, text="Tạo báo cáo", command=on_button_click)
    button.pack(pady=20)

    root.mainloop()

# Gọi hàm tạo GUI
create_gui()
