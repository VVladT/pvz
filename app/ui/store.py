import pygame

from app.entities.sprite import Sprite


class Store:
    def __init__(self, context, items=None, pos=(2, 2), slot_size=(13, 20), padding=1, margin=(2,1)):
        if items is None:
            items = []
        self.context = context
        self.items = items[:8] + [None] * (8 - len(items))
        self.pos = (pos[0] + margin[0], pos[1] + margin[1])
        self.slot_size = slot_size
        self.padding = padding
        self.margin = margin
        self.slots = []
        self.hover_index = None
        self.selected_index = None


    def add_item(self, item):
        for i, slot in enumerate(self.items):
            if slot is None:
                self.items[i] = item
                break

    def get_item(self):
        if self.selected_index is not None:
            return self.items[self.selected_index]
        return None

    def create_slots(self):
        x, y = self.pos
        for i in range(len(self.items)):
            rect = pygame.Rect(x + i*(self.slot_size[0] + self.padding), y, self.slot_size[0], self.slot_size[1])
            self.slots.append(rect)

    def update_hover(self, mouse_pos):
        self.hover_index = None

        for i, slot in enumerate(self.slots):
            item = self.items[i]
            if item is not None and slot.collidepoint(mouse_pos):
                self.hover_index = i
                if not self.is_disabled(item):
                    self.context.mouse.set_state("pointer")
                return

    def update_select(self, mouse_pos):
        for i, slot in enumerate(self.slots):
            item = self.items[i]
            if item is not None and slot.collidepoint(mouse_pos):
                if not self.is_disabled(item):
                    self.selected_index = i
                return

    def is_disabled(self, item):
        return self.context.sun_manager.total < item.price

    def draw(self, surface):
        margin_left, margin_top = self.margin
        store_width = (self.slot_size[0] + self.padding) * len(self.items) - self.padding
        store_height = self.slot_size[1]

        store_rect = pygame.Rect(self.pos[0] - margin_left, self.pos[1] - margin_top, store_width + margin_left * 2,
                                 store_height + margin_top * 2 + 1)
        shadow_store_rect = store_rect.move(0, 1)
        pygame.draw.rect(surface, (40, 40, 40), shadow_store_rect, border_radius=3)
        pygame.draw.rect(surface, (171, 82, 54), store_rect, border_radius=3)

        for i, slot in enumerate(self.slots):
            item = self.items[i]

            shadow_slot = slot.move(0, 1)
            pygame.draw.rect(surface, (40, 40, 40), shadow_slot, border_radius=3)

            if self.hover_index == i:
                pygame.draw.rect(surface, (255, 255, 255), slot.inflate(2, 2), 3, border_radius=3)

            if self.selected_index == i:
                pygame.draw.rect(surface, (255, 255, 0), slot.inflate(2, 2), 3, border_radius=3)
                self.context.mouse.set_state("selected")

            color = (123, 37, 83) if item is None else (255, 204, 170)

            pygame.draw.rect(surface, color, slot, border_radius=3)
            pygame.draw.rect(surface, (131, 118, 156), slot, 1, border_radius=3)

            if item:
                item.draw(surface, (slot.x, slot.y), (slot.width, slot.height))

class Item:
    def __init__(self, context, name, price, icon_data):
        self.name = name
        self.price = price
        self.context = context
        self.icon_data = icon_data
        self.cooldown = 0
        self.font = pygame.font.Font("assets/fonts/main.ttf", 16)

    def draw(self, surface, pos, size):
        icon = Sprite(self.icon_data["frames"][0], self.icon_data["size"], self.context.spritesheet, True)

        icon_pos = (pos[0] + (size[0] - icon.size[0]) // 2, pos[1] + (size[1] - icon.size[1]) // 2 - 3)
        icon.draw(surface, icon_pos)

        if self.context.sun_manager.total >= self.price:
            price_color = (29, 43, 83)
        else:
            price_color = (150, 0, 0)

        price_text = self.font.render(str(self.price), True, price_color)
        price_pos = (pos[0] + (size[0] - price_text.get_width()) // 2 + 1, pos[1] + size[1] - price_text.get_height() - 1)
        surface.blit(price_text, price_pos)
