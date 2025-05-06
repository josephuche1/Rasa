import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export const Logo: React.FC = () => {
  return (
    <View style={styles.container}>
      <View style={styles.logoContainer}>
        <Text style={styles.logoText}>RASA</Text>
        <View style={styles.waveContainer}>
          <View style={[styles.wave, styles.wave1]} />
          <View style={[styles.wave, styles.wave2]} />
          <View style={[styles.wave, styles.wave3]} />
        </View>
      </View>
      <Text style={styles.subtitle}>AI Assistant</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    paddingTop: 40,
    paddingBottom: 20,
  },
  logoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 5,
  },
  logoText: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#2C3E50',
    letterSpacing: 2,
  },
  waveContainer: {
    marginLeft: 10,
    height: 30,
    justifyContent: 'center',
  },
  wave: {
    position: 'absolute',
    width: 20,
    height: 3,
    backgroundColor: '#3498DB',
    borderRadius: 2,
  },
  wave1: {
    transform: [{ translateY: -8 }],
    opacity: 0.8,
  },
  wave2: {
    transform: [{ translateY: 0 }],
    opacity: 0.6,
  },
  wave3: {
    transform: [{ translateY: 8 }],
    opacity: 0.4,
  },
  subtitle: {
    fontSize: 16,
    color: '#7F8C8D',
    letterSpacing: 1,
  },
}); 