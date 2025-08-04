import unittest
from television import *


class Test(unittest.TestCase):

    def setUp(self):
        self.tv1 = Television()


    def tearDown(self):
        del self.tv1


    def test_init(self):
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')


    def test_power(self):
        self.tv1.power()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 0')
        self.tv1.power()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')


    def test_mute(self):
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.tv1.power()
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 0')
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.tv1.power()
        self.tv1.mute()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 1')


    def test_channel_up(self):
        self.tv1.channel_up()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.tv1.power()
        self.tv1.channel_up()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 1, Volume = 0')
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 0')

    def test_channel_down(self):
        self.tv1.channel_down()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.tv1.power()
        self.tv1.channel_down()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 3, Volume = 0')
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 0')

    def test_volume_up(self):
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.tv1.power()
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.tv1.mute()
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 2')
        self.tv1.volume_up()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 2')

    def test_volume_down(self):
        self.tv1.volume_down()
        self.assertEqual(self.tv1.__str__(), 'Power = False, Channel = 0, Volume = 0')
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 1')
        self.tv1.mute()
        self.tv1.volume_down()
        self.assertEqual(self.tv1.__str__(), 'Power = True, Channel = 0, Volume = 0')



if __name__ == '__main__':
    unittest.main()
