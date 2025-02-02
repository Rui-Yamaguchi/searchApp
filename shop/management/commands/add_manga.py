from django.core.management.base import BaseCommand
from shop.models import Book

class Command(BaseCommand):
    help = 'Add manga information to the database with specified image names'

    def handle(self, *args, **kwargs):
        mangas = [
            {'title': '暗殺教室', 'author': '松井優征', 'price': 620, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'ansatukyousitu.jpg'},
            {'title': 'アオハライド', 'author': '咲坂伊緒', 'price': 600, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'aoharaido.jpg'},
            {'title': '僕のヒーローアカデミア', 'author': '堀越耕平', 'price': 780, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'bokunohiroakademia.jpg'},
            {'title': 'チェンソーマン', 'author': '藤本タツキ', 'price': 440, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'chiensoman.jpg'},
            {'title': 'Dr.STONE', 'author': '稲垣理一郎', 'price': 510, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'dokuta-suto-nn.jpg'},
            {'title': 'ドラゴンボール', 'author': '鳥山明', 'price': 500, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'doragonnbo-ru.jpg'},
            {'title': '銀魂', 'author': '空知英秋', 'price': 390, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'gintama.jpg'},
            {'title': 'ゴールデンカムイ', 'author': '野田サトル', 'price': 580, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'go-rudennkamui.jpg'},
            {'title': '五等分の花嫁', 'author': '春場ねぎ', 'price': 450, 'volume_number': 1, 'publisher': '講談社', 'image_name': 'gotoubunnnohanayome.jpg'},
            {'title': 'ハイキュー!!', 'author': '古舘春一', 'price': 730, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'haikyu-.jpg'},
            {'title': 'HUNTEER×HUNTEER', 'author': '冨樫義博', 'price': 400, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'hanta-hanta-.jpg'},
            {'title': 'はたらく細胞', 'author': '清水茜', 'price': 600, 'volume_number': 1, 'publisher': '講談社', 'image_name': 'hatarakusaibou.jpg'},
            {'title': '賭ケグルイ', 'author': '河本ほむら', 'price': 580, 'volume_number': 1, 'publisher': 'スクウェア・エニックス', 'image_name': 'kakegurui.jpg'},
            {'title': 'からかい上手の高木さん', 'author': '山本崇一朗', 'price': 490, 'volume_number': 1, 'publisher': '小学館', 'image_name': 'karakaijozunotakagisan.jpg'},
            {'title': '鬼滅の刃', 'author': '吾峠呼世晴', 'price': 460, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'kimetsunoyaiba.jpg'},
            {'title': 'キングダム', 'author': '原泰久', 'price': 560, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'kingdom.jpg'},
            {'title': '名探偵コナン', 'author': '青山剛昌', 'price': 420, 'volume_number': 1, 'publisher': '小学館', 'image_name': 'konann.jpg'},
            {'title': 'こちら葛飾区亀有公園前派出所', 'author': '秋本治', 'price': 760, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'kotikame.jpg'},
            {'title': 'NANA', 'author': '矢沢あい', 'price': 500, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'nana.jpg'},
            {'title': 'NARUTO -ナルト-', 'author': '岸本斉史', 'price': 420, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'naruto.jpg'},
            {'title': '【推しの子】', 'author': '赤坂アカ & 横槍メンゴ', 'price': 650, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'oshinoko.jpg'},
            {'title': 'SPY×FAMILY', 'author': '遠藤達哉', 'price': 500, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'spy_family.jpg'},
            {'title': 'スラムダンク', 'author': '井上雄彦', 'price': 700, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'suramudanku.jpg'},
            {'title': 'ちはやふる', 'author': '末次由紀', 'price': 480, 'volume_number': 1, 'publisher': '講談社', 'image_name': 'tihayahuru.jpg'},
            {'title': '東京卍リベンジャーズ', 'author': '和久井健', 'price': 510, 'volume_number': 1, 'publisher': '講談社', 'image_name': 'tokyo_ribennja-zu.jpg'},
            {'title': 'トリコ', 'author': '島袋光年', 'price': 620, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'toriko.jpg'},
            {'title': '東京喰種トーキョーグール', 'author': '石田スイ', 'price': 630, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'toukyougu-ru.jpg'},
            {'title': 'ONE PIECE', 'author': '尾田栄一郎', 'price': 420, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'wannpi-su.jpg'},
            {'title': '約束のネバーランド', 'author': '白井カイウ & 出水ぽすか', 'price': 560, 'volume_number': 1, 'publisher': '集英社', 'image_name': 'yakusokunoneba-rando.jpg'},
            {'title': '妖怪ウォッチ', 'author': '小西紀行', 'price': 450, 'volume_number': 1, 'publisher': '小学館', 'image_name': 'youkaiwhotti.jpg'},
        ]

        for manga in mangas:
            Book.objects.create(**manga)
            self.stdout.write(f"Added {manga['title']} - Volume {manga['volume_number']}")

        self.stdout.write(self.style.SUCCESS("Successfully added all manga volumes with specified image names"))