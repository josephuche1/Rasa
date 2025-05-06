import axios from 'axios';

const RASA_API_URL = 'http://10.0.2.2:5005/webhooks/rest/webhook';

export interface RasaMessage {
  message: string;
  sender: string;
}

export interface RasaResponse {
  recipient_id: string;
  text: string;
}

export const sendMessage = async (message: string): Promise<RasaResponse[]> => {
  try {
    const response = await axios.post(RASA_API_URL, {
      sender: 'user',
      message: message,
    });
    return response.data;
  } catch (error) {
    console.error('Error sending message to RASA:', error);
    throw error;
  }
}; 