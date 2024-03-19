import { StyleSheet, Image } from 'react-native';
import EditScreenInfo from '@/src/components/EditScreenInfo';
import { Text, View } from '@/src/components/Themed';

import { vocabs } from '@/assets/data/vocabs';

const vocab = vocabs[0]

export default function TabOneScreen() {
  return (
    <View style={styles.container}>
      <Image source={vocab.img}/>
      <Text>{vocab.pinyin}</Text>
      <Text style={styles.title}>{vocab.simplifiedChinese}</Text>
      <Text style={styles.meaning}>{vocab.meaning}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 40,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
  meaning: {
    fontSize: 20,
  }
});
