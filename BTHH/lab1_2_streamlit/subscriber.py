import paho.mqtt.client as mqtt

# Hàm xử lý khi kết nối thành công tới MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Kết nối MQTT thành công!")
        client.subscribe("iot/khdl/esp32")
    else:
        print("❌ Lỗi kết nối, mã lỗi:", rc)

# Hàm xử lý khi nhận được tin nhắn
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# Tạo client và cấu hình callback
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Kết nối đến broker và bắt đầu vòng lặp
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
