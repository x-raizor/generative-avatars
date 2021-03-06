// Here is code for smile generation in Processing. Download it at http://processing.org/

int fontsize = 120*2;
int erase_after = 10;

PFont captions;
String[] fontList = PFont.list();

int font_num = fontList.length;

char[] noses = {
    '-', '·', '*'
};
char[] eyes = {
    ':', ';', '|'
};
char[] mouths = {
    ')', '|', 'P', ']', '/'
};

int noses_num = noses.length;
int eyes_num = eyes.length;
int mouths_num = mouths.length;

void setup() {

    size(1440, 900);
    smooth();
    background(0);
    noStroke();
    fill(0, 0, 0, 255);

    frameRate(0.75);
}

void draw() {

    draw_smile();

}


void draw_smile() {
    
    background(0);
    String fontname = fontList[int(random(font_num))];

    captions = createFont(fontname, fontsize);
    textFont(captions);
    fill(230);

    String nose = String.valueOf(noses[int(random(noses_num))]);
    String eye = String.valueOf(eyes[int(random(eyes_num))]);
    String mouth = String.valueOf(mouths[int(random(mouths_num))]);

    String face = eye + nose + mouth;

    translate(width/2 - fontsize/4, height/2); 
    rotate(PI/2);
    textAlign(CENTER);
    text(face, 0, 0);

    fill(80);
    captions = createFont(fontname, fontsize/16);
    textFont(captions);
    rotate(PI);
    translate(0, height/2);
    textAlign(CENTER);
    text(fontname, 0, 0);
}