#include <pebble.h>

Window *window;
TextLayer *text_layer;


void handle_init(void){
   window = window_create();
   Layer *window_layer = window_get_root_layer(window);
   GRect bounds = layer_get_bounds(window_layer);
   text_layer = text_layer_create(GRect(0,PBL_IF_ROUND_ELSE(58,52), bounds.size.w,50));
   

   text_layer_set_text(text_layer, "RAF rocks");
   text_layer_set_font(text_layer, fonts_get_system_font(FONT_KEY_GOTHIC_28_BOLD));
   text_layer_set_text_alignment(text_layer, GTextAlignmentCenter);
   text_layer_set_background_color(text_layer, GColorWhite);   
   layer_add_child(window_get_root_layer(window), text_layer_get_layer(text_layer));
   
  window_stack_push(window, true);
}

void handle_deinit(void){
  text_layer_destroy(text_layer);

  window_destroy(window);

}

int main(void){
  handle_init();
  app_event_loop();
  handle_deinit();
}
