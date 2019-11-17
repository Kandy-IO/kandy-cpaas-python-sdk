from .twofactor import Twofactor
from .conversation import Conversation
from .notification import Notification

list = {
  'twofactor': Twofactor,
  'conversation': Conversation,
  'notification': Notification
}
