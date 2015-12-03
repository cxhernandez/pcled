#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6 // Data PIN
#define NUM 60 // Number of LEDs
#define PORT 9600 // Port Address

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM, PIN, NEO_GRB + NEO_KHZ800);

int j;
int wait = 10;
String msg;

int RGB[3] = {0, 0, 150}; // Default color: Blue
uint32_t C = strip.Color(RGB[0], RGB[1], RGB[2]);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 301 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  j = 0;
  msg = "";

  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

  Serial.begin(PORT);
  Serial.write(1);
}

void loop() {
  j = j % NUM;
  exec(j);
  j++;
  }

  void exec(int j) {
    if (Serial.available()) {
      Serial.write(0);
      char ch = Serial.read();
      if (ch >= '0' && ch <= '9') {
        msg += ch;
      } else {
        int code = getCode(ch);
        if (code > -1 && code < 3) {
          setRGB(msg, code);
          msg = "";
        } else if (code == 3) {
          wait = msg.toInt();
          Serial.write(1);
        }
      }
    }
    strip.setPixelColor(j, C);
    strip.show();
    delay(wait);
  }

  int getCode(char ch) {
    if (ch == 'r') {
      return 0;
    }
    if (ch == 'g') {
      return 1;
    }
    if (ch == 'b') {
      return 2;
    }
    if (ch == 'c') {
      return 3;
    }
    return -1;
  }


  void setRGB(String msg, int code) {
      RGB[code] = msg.toInt();
      if (code == 2) {
        C = strip.Color(RGB[0], RGB[1], RGB[2]);
        Serial.write(1);
      }
  }
