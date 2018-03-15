# coding: utf-8
from PIL import ImageFont, ImageDraw
import six

class TextCompositor:
    BOLD_LOOP_COUNT = 20 # Boldを再現するループ描画数

    def __init__(self, string, font_size, draw_start_x, draw_start_y, is_bold=False, font_color='#ffffff'):
        self.__string       = string       # 対象文字列
        self.__font_size    = font_size    # フォントサイズ
        self.__draw_start_x = draw_start_x # 描画開始位置X
        self.__draw_start_y = draw_start_y # 描画開始位置Y
        self.__bold         = is_bold      # Boldを行うかどうかのフラグ
        self.__font_color   = font_color   # 文字色


    def getFontfilePath(self):
        return './font.otf'


    def getString(self):
        if (six.PY2 == True):
            # python2系の場合は、unicode変換をかける
            return unicode(self.__string, 'utf-8', 'ignore')

        return self.__string


    def isBold(self):
        return self.__bold


    def composite(self, frame_image, font_color='#ffffff'):
        # 描画用データを取得
        draw_image = ImageDraw.Draw(frame_image)

        # フォントデータを取得
        image_font = ImageFont.truetype(self.getFontfilePath(), self.__font_size)

        if (self.isBold() == True):
            # Bold判定の場合は指定回数分ループして同じ箇所に描画し続ける
            for i in range(self.BOLD_LOOP_COUNT):
                self.__execute(draw_image, image_font)
        else:
            self.__execute(draw_image, image_font)


    def __execute(self, draw_image, image_font):
        # 各文字の描画管理変数
        ix, iy = 0, 0

        for c in self.getString():
            x = self.__draw_start_x - ix * self.__font_size
            y = self.__draw_start_y + (iy * self.__font_size)

            # 今回描画する1文字の詳細なX, Yを設定
            char_width, char_height = image_font.getsize(c)
            x += (self.__font_size - char_width) / 2
            y += self.__draw_start_y

            # 指定の場所へ文字を描画
            draw_image.text((x, y), c, font=image_font, fill=self.__font_color)

            # 次の文字へ
            iy += 1
