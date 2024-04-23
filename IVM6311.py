
class System_CTRL :
    
    def __init__(self) -> None:
        self.address = 0x0
        self.page = 0
        
    @property
    def fro_sel_0p8125mhz(self):
        self.fro_sel_0p8125mhz_pos   = 3
        self.fro_sel_0p8125mhz_len   = 1
        return self.fro_sel_0p8125mhz_value
        
    @fro_sel_0p8125mhz.setter
    def fro_sel_0p8125mhz(self,value):
        self.fro_sel_0p8125mhz_value = value 
        regvalue = self.fro_sel_0p8125mhz
        # perform operation with reg value 
            
    @property
    def fro_sel_1p625mhz(self):
        self.fro_sel_1p625mhz_pos   = 2
        self.fro_sel_1p625mhz_len   = 1
        return self.fro_sel_1p625mhz_value
        
    @fro_sel_1p625mhz.setter
    def fro_sel_1p625mhz(self,value):
        self.fro_sel_1p625mhz_value = value 
        regvalue = self.fro_sel_1p625mhz
        # perform operation with reg value 
            
    @property
    def fro_sel(self):
        self.fro_sel_pos   = 1
        self.fro_sel_len   = 1
        return self.fro_sel_value
        
    @fro_sel.setter
    def fro_sel(self,value):
        self.fro_sel_value = value 
        regvalue = self.fro_sel
        # perform operation with reg value 
            
    @property
    def powerup(self):
        self.powerup_pos   = 0
        self.powerup_len   = 1
        return self.powerup_value
        
    @powerup.setter
    def powerup(self,value):
        self.powerup_value = value 
        regvalue = self.powerup
        # perform operation with reg value 
             
class Software_reset :
    
    def __init__(self) -> None:
        self.address = 0x1
        self.page = 0
        
    @property
    def hard_reset(self):
        self.hard_reset_pos   = 0
        self.hard_reset_len   = 1
        return self.hard_reset_value
        
    @hard_reset.setter
    def hard_reset(self,value):
        self.hard_reset_value = value 
        regvalue = self.hard_reset
        # perform operation with reg value 
             
class Interrupt_management :
    
    def __init__(self) -> None:
        self.address = 0x2
        self.page = 0
        
    @property
    def general_fault_aon(self):
        self.general_fault_aon_pos   = 3
        self.general_fault_aon_len   = 1
        return self.general_fault_aon_value
        
    @general_fault_aon.setter
    def general_fault_aon(self,value):
        self.general_fault_aon_value = value 
        regvalue = self.general_fault_aon
        # perform operation with reg value 
            
    @property
    def int_mask_mode(self):
        self.int_mask_mode_pos   = 2
        self.int_mask_mode_len   = 1
        return self.int_mask_mode_value
        
    @int_mask_mode.setter
    def int_mask_mode(self,value):
        self.int_mask_mode_value = value 
        regvalue = self.int_mask_mode
        # perform operation with reg value 
            
    @property
    def int_polarity(self):
        self.int_polarity_pos   = 1
        self.int_polarity_len   = 1
        return self.int_polarity_value
        
    @int_polarity.setter
    def int_polarity(self,value):
        self.int_polarity_value = value 
        regvalue = self.int_polarity
        # perform operation with reg value 
            
    @property
    def int_clear_mode(self):
        self.int_clear_mode_pos   = 0
        self.int_clear_mode_len   = 1
        return self.int_clear_mode_value
        
    @int_clear_mode.setter
    def int_clear_mode(self,value):
        self.int_clear_mode_value = value 
        regvalue = self.int_clear_mode
        # perform operation with reg value 
             
class Interrupt_status_register_1 :
    
    def __init__(self) -> None:
        self.address = 0x3
        self.page = 0
        
    @property
    def audio_en_int(self):
        self.audio_en_int_pos   = 7
        self.audio_en_int_len   = 1
        return self.audio_en_int_value
        
    @audio_en_int.setter
    def audio_en_int(self,value):
        self.audio_en_int_value = value 
        regvalue = self.audio_en_int
        # perform operation with reg value 
            
    @property
    def pa_ng_on_int(self):
        self.pa_ng_on_int_pos   = 6
        self.pa_ng_on_int_len   = 1
        return self.pa_ng_on_int_value
        
    @pa_ng_on_int.setter
    def pa_ng_on_int(self,value):
        self.pa_ng_on_int_value = value 
        regvalue = self.pa_ng_on_int
        # perform operation with reg value 
            
    @property
    def pa_ng_off_int(self):
        self.pa_ng_off_int_pos   = 5
        self.pa_ng_off_int_len   = 1
        return self.pa_ng_off_int_value
        
    @pa_ng_off_int.setter
    def pa_ng_off_int(self,value):
        self.pa_ng_off_int_value = value 
        regvalue = self.pa_ng_off_int
        # perform operation with reg value 
            
    @property
    def fsyn_valid_fault(self):
        self.fsyn_valid_fault_pos   = 4
        self.fsyn_valid_fault_len   = 1
        return self.fsyn_valid_fault_value
        
    @fsyn_valid_fault.setter
    def fsyn_valid_fault(self,value):
        self.fsyn_valid_fault_value = value 
        regvalue = self.fsyn_valid_fault
        # perform operation with reg value 
            
    @property
    def tdm_i_fault(self):
        self.tdm_i_fault_pos   = 3
        self.tdm_i_fault_len   = 1
        return self.tdm_i_fault_value
        
    @tdm_i_fault.setter
    def tdm_i_fault(self,value):
        self.tdm_i_fault_value = value 
        regvalue = self.tdm_i_fault
        # perform operation with reg value 
            
    @property
    def tsd_fault(self):
        self.tsd_fault_pos   = 2
        self.tsd_fault_len   = 1
        return self.tsd_fault_value
        
    @tsd_fault.setter
    def tsd_fault(self,value):
        self.tsd_fault_value = value 
        regvalue = self.tsd_fault
        # perform operation with reg value 
            
    @property
    def pwrok_fault(self):
        self.pwrok_fault_pos   = 1
        self.pwrok_fault_len   = 1
        return self.pwrok_fault_value
        
    @pwrok_fault.setter
    def pwrok_fault(self,value):
        self.pwrok_fault_value = value 
        regvalue = self.pwrok_fault
        # perform operation with reg value 
            
    @property
    def clk_missing_fault(self):
        self.clk_missing_fault_pos   = 0
        self.clk_missing_fault_len   = 1
        return self.clk_missing_fault_value
        
    @clk_missing_fault.setter
    def clk_missing_fault(self,value):
        self.clk_missing_fault_value = value 
        regvalue = self.clk_missing_fault
        # perform operation with reg value 
             
class Interrupt_mask_register_1 :
    
    def __init__(self) -> None:
        self.address = 0x4
        self.page = 0
        
    @property
    def audio_en_int_mask(self):
        self.audio_en_int_mask_pos   = 7
        self.audio_en_int_mask_len   = 1
        return self.audio_en_int_mask_value
        
    @audio_en_int_mask.setter
    def audio_en_int_mask(self,value):
        self.audio_en_int_mask_value = value 
        regvalue = self.audio_en_int_mask
        # perform operation with reg value 
            
    @property
    def pa_ng_on_int_mask(self):
        self.pa_ng_on_int_mask_pos   = 6
        self.pa_ng_on_int_mask_len   = 1
        return self.pa_ng_on_int_mask_value
        
    @pa_ng_on_int_mask.setter
    def pa_ng_on_int_mask(self,value):
        self.pa_ng_on_int_mask_value = value 
        regvalue = self.pa_ng_on_int_mask
        # perform operation with reg value 
            
    @property
    def pa_ng_off_int_mask(self):
        self.pa_ng_off_int_mask_pos   = 5
        self.pa_ng_off_int_mask_len   = 1
        return self.pa_ng_off_int_mask_value
        
    @pa_ng_off_int_mask.setter
    def pa_ng_off_int_mask(self,value):
        self.pa_ng_off_int_mask_value = value 
        regvalue = self.pa_ng_off_int_mask
        # perform operation with reg value 
            
    @property
    def fsyn_valid_fault_mask(self):
        self.fsyn_valid_fault_mask_pos   = 4
        self.fsyn_valid_fault_mask_len   = 1
        return self.fsyn_valid_fault_mask_value
        
    @fsyn_valid_fault_mask.setter
    def fsyn_valid_fault_mask(self,value):
        self.fsyn_valid_fault_mask_value = value 
        regvalue = self.fsyn_valid_fault_mask
        # perform operation with reg value 
            
    @property
    def tdm_i_fault_mask(self):
        self.tdm_i_fault_mask_pos   = 3
        self.tdm_i_fault_mask_len   = 1
        return self.tdm_i_fault_mask_value
        
    @tdm_i_fault_mask.setter
    def tdm_i_fault_mask(self,value):
        self.tdm_i_fault_mask_value = value 
        regvalue = self.tdm_i_fault_mask
        # perform operation with reg value 
            
    @property
    def tsd_fault_mask(self):
        self.tsd_fault_mask_pos   = 2
        self.tsd_fault_mask_len   = 1
        return self.tsd_fault_mask_value
        
    @tsd_fault_mask.setter
    def tsd_fault_mask(self,value):
        self.tsd_fault_mask_value = value 
        regvalue = self.tsd_fault_mask
        # perform operation with reg value 
            
    @property
    def pwrok_fault_mask(self):
        self.pwrok_fault_mask_pos   = 1
        self.pwrok_fault_mask_len   = 1
        return self.pwrok_fault_mask_value
        
    @pwrok_fault_mask.setter
    def pwrok_fault_mask(self,value):
        self.pwrok_fault_mask_value = value 
        regvalue = self.pwrok_fault_mask
        # perform operation with reg value 
            
    @property
    def clk_missing_fault_mask(self):
        self.clk_missing_fault_mask_pos   = 0
        self.clk_missing_fault_mask_len   = 1
        return self.clk_missing_fault_mask_value
        
    @clk_missing_fault_mask.setter
    def clk_missing_fault_mask(self,value):
        self.clk_missing_fault_mask_value = value 
        regvalue = self.clk_missing_fault_mask
        # perform operation with reg value 
             
class Interrupt_status_register_2 :
    
    def __init__(self) -> None:
        self.address = 0x5
        self.page = 0
        
    @property
    def fir4_clip_fault(self):
        self.fir4_clip_fault_pos   = 6
        self.fir4_clip_fault_len   = 1
        return self.fir4_clip_fault_value
        
    @fir4_clip_fault.setter
    def fir4_clip_fault(self,value):
        self.fir4_clip_fault_value = value 
        regvalue = self.fir4_clip_fault
        # perform operation with reg value 
            
    @property
    def fir3_clip_fault(self):
        self.fir3_clip_fault_pos   = 5
        self.fir3_clip_fault_len   = 1
        return self.fir3_clip_fault_value
        
    @fir3_clip_fault.setter
    def fir3_clip_fault(self,value):
        self.fir3_clip_fault_value = value 
        regvalue = self.fir3_clip_fault
        # perform operation with reg value 
            
    @property
    def fir2_clip_fault(self):
        self.fir2_clip_fault_pos   = 4
        self.fir2_clip_fault_len   = 1
        return self.fir2_clip_fault_value
        
    @fir2_clip_fault.setter
    def fir2_clip_fault(self,value):
        self.fir2_clip_fault_value = value 
        regvalue = self.fir2_clip_fault
        # perform operation with reg value 
            
    @property
    def fir1_clip_fault(self):
        self.fir1_clip_fault_pos   = 3
        self.fir1_clip_fault_len   = 1
        return self.fir1_clip_fault_value
        
    @fir1_clip_fault.setter
    def fir1_clip_fault(self,value):
        self.fir1_clip_fault_value = value 
        regvalue = self.fir1_clip_fault
        # perform operation with reg value 
            
    @property
    def bst_ocp_fault(self):
        self.bst_ocp_fault_pos   = 2
        self.bst_ocp_fault_len   = 1
        return self.bst_ocp_fault_value
        
    @bst_ocp_fault.setter
    def bst_ocp_fault(self,value):
        self.bst_ocp_fault_value = value 
        regvalue = self.bst_ocp_fault
        # perform operation with reg value 
            
    @property
    def bst_bias_ovp_fault(self):
        self.bst_bias_ovp_fault_pos   = 1
        self.bst_bias_ovp_fault_len   = 1
        return self.bst_bias_ovp_fault_value
        
    @bst_bias_ovp_fault.setter
    def bst_bias_ovp_fault(self,value):
        self.bst_bias_ovp_fault_value = value 
        regvalue = self.bst_bias_ovp_fault
        # perform operation with reg value 
            
    @property
    def bst_bso_ovp_fault(self):
        self.bst_bso_ovp_fault_pos   = 0
        self.bst_bso_ovp_fault_len   = 1
        return self.bst_bso_ovp_fault_value
        
    @bst_bso_ovp_fault.setter
    def bst_bso_ovp_fault(self,value):
        self.bst_bso_ovp_fault_value = value 
        regvalue = self.bst_bso_ovp_fault
        # perform operation with reg value 
             
class Interrupt_mask_register_2 :
    
    def __init__(self) -> None:
        self.address = 0x6
        self.page = 0
        
    @property
    def fir4_clip_fault_mask(self):
        self.fir4_clip_fault_mask_pos   = 6
        self.fir4_clip_fault_mask_len   = 1
        return self.fir4_clip_fault_mask_value
        
    @fir4_clip_fault_mask.setter
    def fir4_clip_fault_mask(self,value):
        self.fir4_clip_fault_mask_value = value 
        regvalue = self.fir4_clip_fault_mask
        # perform operation with reg value 
            
    @property
    def fir3_clip_fault_mask(self):
        self.fir3_clip_fault_mask_pos   = 5
        self.fir3_clip_fault_mask_len   = 1
        return self.fir3_clip_fault_mask_value
        
    @fir3_clip_fault_mask.setter
    def fir3_clip_fault_mask(self,value):
        self.fir3_clip_fault_mask_value = value 
        regvalue = self.fir3_clip_fault_mask
        # perform operation with reg value 
            
    @property
    def fir2_clip_fault_mask(self):
        self.fir2_clip_fault_mask_pos   = 4
        self.fir2_clip_fault_mask_len   = 1
        return self.fir2_clip_fault_mask_value
        
    @fir2_clip_fault_mask.setter
    def fir2_clip_fault_mask(self,value):
        self.fir2_clip_fault_mask_value = value 
        regvalue = self.fir2_clip_fault_mask
        # perform operation with reg value 
            
    @property
    def fir1_clip_fault_mask(self):
        self.fir1_clip_fault_mask_pos   = 3
        self.fir1_clip_fault_mask_len   = 1
        return self.fir1_clip_fault_mask_value
        
    @fir1_clip_fault_mask.setter
    def fir1_clip_fault_mask(self,value):
        self.fir1_clip_fault_mask_value = value 
        regvalue = self.fir1_clip_fault_mask
        # perform operation with reg value 
            
    @property
    def bst_ocp_fault_mask(self):
        self.bst_ocp_fault_mask_pos   = 2
        self.bst_ocp_fault_mask_len   = 1
        return self.bst_ocp_fault_mask_value
        
    @bst_ocp_fault_mask.setter
    def bst_ocp_fault_mask(self,value):
        self.bst_ocp_fault_mask_value = value 
        regvalue = self.bst_ocp_fault_mask
        # perform operation with reg value 
            
    @property
    def bst_bias_ovp_fault_mask(self):
        self.bst_bias_ovp_fault_mask_pos   = 1
        self.bst_bias_ovp_fault_mask_len   = 1
        return self.bst_bias_ovp_fault_mask_value
        
    @bst_bias_ovp_fault_mask.setter
    def bst_bias_ovp_fault_mask(self,value):
        self.bst_bias_ovp_fault_mask_value = value 
        regvalue = self.bst_bias_ovp_fault_mask
        # perform operation with reg value 
            
    @property
    def bst_bso_ovp_fault_mask(self):
        self.bst_bso_ovp_fault_mask_pos   = 0
        self.bst_bso_ovp_fault_mask_len   = 1
        return self.bst_bso_ovp_fault_mask_value
        
    @bst_bso_ovp_fault_mask.setter
    def bst_bso_ovp_fault_mask(self,value):
        self.bst_bso_ovp_fault_mask_value = value 
        regvalue = self.bst_bso_ovp_fault_mask
        # perform operation with reg value 
             
class Status_register_1 :
    
    def __init__(self) -> None:
        self.address = 0xa
        self.page = 0
        
    @property
    def bst_byp_on(self):
        self.bst_byp_on_pos   = 7
        self.bst_byp_on_len   = 1
        return self.bst_byp_on_value
        
    @bst_byp_on.setter
    def bst_byp_on(self,value):
        self.bst_byp_on_value = value 
        regvalue = self.bst_byp_on
        # perform operation with reg value 
            
    @property
    def classd_ng_on(self):
        self.classd_ng_on_pos   = 6
        self.classd_ng_on_len   = 1
        return self.classd_ng_on_value
        
    @classd_ng_on.setter
    def classd_ng_on(self,value):
        self.classd_ng_on_value = value 
        regvalue = self.classd_ng_on
        # perform operation with reg value 
            
    @property
    def fsyn_valid(self):
        self.fsyn_valid_pos   = 4
        self.fsyn_valid_len   = 1
        return self.fsyn_valid_value
        
    @fsyn_valid.setter
    def fsyn_valid(self,value):
        self.fsyn_valid_value = value 
        regvalue = self.fsyn_valid
        # perform operation with reg value 
            
    @property
    def tdm_i(self):
        self.tdm_i_pos   = 3
        self.tdm_i_len   = 1
        return self.tdm_i_value
        
    @tdm_i.setter
    def tdm_i(self,value):
        self.tdm_i_value = value 
        regvalue = self.tdm_i
        # perform operation with reg value 
            
    @property
    def tsd(self):
        self.tsd_pos   = 2
        self.tsd_len   = 1
        return self.tsd_value
        
    @tsd.setter
    def tsd(self,value):
        self.tsd_value = value 
        regvalue = self.tsd
        # perform operation with reg value 
            
    @property
    def pwrok(self):
        self.pwrok_pos   = 1
        self.pwrok_len   = 1
        return self.pwrok_value
        
    @pwrok.setter
    def pwrok(self,value):
        self.pwrok_value = value 
        regvalue = self.pwrok
        # perform operation with reg value 
            
    @property
    def clk_missing(self):
        self.clk_missing_pos   = 0
        self.clk_missing_len   = 1
        return self.clk_missing_value
        
    @clk_missing.setter
    def clk_missing(self,value):
        self.clk_missing_value = value 
        regvalue = self.clk_missing
        # perform operation with reg value 
             
class Status_register_2 :
    
    def __init__(self) -> None:
        self.address = 0xb
        self.page = 0
        
    @property
    def audio_en(self):
        self.audio_en_pos   = 7
        self.audio_en_len   = 1
        return self.audio_en_value
        
    @audio_en.setter
    def audio_en(self,value):
        self.audio_en_value = value 
        regvalue = self.audio_en
        # perform operation with reg value 
            
    @property
    def bst_bias_ovp(self):
        self.bst_bias_ovp_pos   = 1
        self.bst_bias_ovp_len   = 1
        return self.bst_bias_ovp_value
        
    @bst_bias_ovp.setter
    def bst_bias_ovp(self,value):
        self.bst_bias_ovp_value = value 
        regvalue = self.bst_bias_ovp
        # perform operation with reg value 
            
    @property
    def bst_bso_ovp(self):
        self.bst_bso_ovp_pos   = 0
        self.bst_bso_ovp_len   = 1
        return self.bst_bso_ovp_value
        
    @bst_bso_ovp.setter
    def bst_bso_ovp(self,value):
        self.bst_bso_ovp_value = value 
        regvalue = self.bst_bso_ovp
        # perform operation with reg value 
             
class Status_register_3 :
    
    def __init__(self) -> None:
        self.address = 0xc
        self.page = 0
        
    @property
    def mnt_fsyn_rate2_0(self):
        self.mnt_fsyn_rate2_0_pos   = 4
        self.mnt_fsyn_rate2_0_len   = 3
        return self.mnt_fsyn_rate2_0_value
        
    @mnt_fsyn_rate2_0.setter
    def mnt_fsyn_rate2_0(self,value):
        self.mnt_fsyn_rate2_0_value = value 
        regvalue = self.mnt_fsyn_rate2_0
        # perform operation with reg value 
            
    @property
    def mnt_bclk_osr2_0(self):
        self.mnt_bclk_osr2_0_pos   = 0
        self.mnt_bclk_osr2_0_len   = 3
        return self.mnt_bclk_osr2_0_value
        
    @mnt_bclk_osr2_0.setter
    def mnt_bclk_osr2_0(self,value):
        self.mnt_bclk_osr2_0_value = value 
        regvalue = self.mnt_bclk_osr2_0
        # perform operation with reg value 
             
class Status_register_4 :
    
    def __init__(self) -> None:
        self.address = 0xd
        self.page = 0
        
    @property
    def platform1_0(self):
        self.platform1_0_pos   = 4
        self.platform1_0_len   = 2
        return self.platform1_0_value
        
    @platform1_0.setter
    def platform1_0(self,value):
        self.platform1_0_value = value 
        regvalue = self.platform1_0
        # perform operation with reg value 
            
    @property
    def boot_done(self):
        self.boot_done_pos   = 0
        self.boot_done_len   = 1
        return self.boot_done_value
        
    @boot_done.setter
    def boot_done(self,value):
        self.boot_done_value = value 
        regvalue = self.boot_done
        # perform operation with reg value 
             
class Status_register_5 :
    
    def __init__(self) -> None:
        self.address = 0xe
        self.page = 0
        
    @property
    def ext_offset_zero_sat(self):
        self.ext_offset_zero_sat_pos   = 7
        self.ext_offset_zero_sat_len   = 1
        return self.ext_offset_zero_sat_value
        
    @ext_offset_zero_sat.setter
    def ext_offset_zero_sat(self,value):
        self.ext_offset_zero_sat_value = value 
        regvalue = self.ext_offset_zero_sat
        # perform operation with reg value 
            
    @property
    def ext_offset_idle_sat(self):
        self.ext_offset_idle_sat_pos   = 6
        self.ext_offset_idle_sat_len   = 1
        return self.ext_offset_idle_sat_value
        
    @ext_offset_idle_sat.setter
    def ext_offset_idle_sat(self,value):
        self.ext_offset_idle_sat_value = value 
        regvalue = self.ext_offset_idle_sat
        # perform operation with reg value 
            
    @property
    def applied_offset11_8(self):
        self.applied_offset11_8_pos   = 0
        self.applied_offset11_8_len   = 4
        return self.applied_offset11_8_value
        
    @applied_offset11_8.setter
    def applied_offset11_8(self,value):
        self.applied_offset11_8_value = value 
        regvalue = self.applied_offset11_8
        # perform operation with reg value 
             
class Status_register_6 :
    
    def __init__(self) -> None:
        self.address = 0xf
        self.page = 0
        
    @property
    def applied_offset7_0(self):
        self.applied_offset7_0_pos   = 0
        self.applied_offset7_0_len   = 8
        return self.applied_offset7_0_value
        
    @applied_offset7_0.setter
    def applied_offset7_0(self,value):
        self.applied_offset7_0_value = value 
        regvalue = self.applied_offset7_0
        # perform operation with reg value 
             
class Enables_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x19
        self.page = 0
        
    @property
    def en_ana_dc_mode(self):
        self.en_ana_dc_mode_pos   = 7
        self.en_ana_dc_mode_len   = 1
        return self.en_ana_dc_mode_value
        
    @en_ana_dc_mode.setter
    def en_ana_dc_mode(self,value):
        self.en_ana_dc_mode_value = value 
        regvalue = self.en_ana_dc_mode
        # perform operation with reg value 
            
    @property
    def i3c_hs_en(self):
        self.i3c_hs_en_pos   = 6
        self.i3c_hs_en_len   = 1
        return self.i3c_hs_en_value
        
    @i3c_hs_en.setter
    def i3c_hs_en(self,value):
        self.i3c_hs_en_value = value 
        regvalue = self.i3c_hs_en
        # perform operation with reg value 
            
    @property
    def tif_en(self):
        self.tif_en_pos   = 4
        self.tif_en_len   = 1
        return self.tif_en_value
        
    @tif_en.setter
    def tif_en(self,value):
        self.tif_en_value = value 
        regvalue = self.tif_en
        # perform operation with reg value 
            
    @property
    def et_en(self):
        self.et_en_pos   = 3
        self.et_en_len   = 1
        return self.et_en_value
        
    @et_en.setter
    def et_en(self,value):
        self.et_en_value = value 
        regvalue = self.et_en
        # perform operation with reg value 
            
    @property
    def refclk_en(self):
        self.refclk_en_pos   = 2
        self.refclk_en_len   = 1
        return self.refclk_en_value
        
    @refclk_en.setter
    def refclk_en(self,value):
        self.refclk_en_value = value 
        regvalue = self.refclk_en
        # perform operation with reg value 
            
    @property
    def mod_en(self):
        self.mod_en_pos   = 1
        self.mod_en_len   = 1
        return self.mod_en_value
        
    @mod_en.setter
    def mod_en(self,value):
        self.mod_en_value = value 
        regvalue = self.mod_en
        # perform operation with reg value 
            
    @property
    def tdm_en(self):
        self.tdm_en_pos   = 0
        self.tdm_en_len   = 1
        return self.tdm_en_value
        
    @tdm_en.setter
    def tdm_en(self,value):
        self.tdm_en_value = value 
        regvalue = self.tdm_en
        # perform operation with reg value 
            
    @property
    def spk_mute(self):
        self.spk_mute_pos   = 1
        self.spk_mute_len   = 1
        return self.spk_mute_value
        
    @spk_mute.setter
    def spk_mute(self,value):
        self.spk_mute_value = value 
        regvalue = self.spk_mute
        # perform operation with reg value 
            
    @property
    def spk_en(self):
        self.spk_en_pos   = 0
        self.spk_en_len   = 1
        return self.spk_en_value
        
    @spk_en.setter
    def spk_en(self,value):
        self.spk_en_value = value 
        regvalue = self.spk_en
        # perform operation with reg value 
             
class Input_selection :
    
    def __init__(self) -> None:
        self.address = 0x11
        self.page = 0
        
    @property
    def pdm_freq1_0(self):
        self.pdm_freq1_0_pos   = 2
        self.pdm_freq1_0_len   = 2
        return self.pdm_freq1_0_value
        
    @pdm_freq1_0.setter
    def pdm_freq1_0(self,value):
        self.pdm_freq1_0_value = value 
        regvalue = self.pdm_freq1_0
        # perform operation with reg value 
            
    @property
    def input_mode1_0(self):
        self.input_mode1_0_pos   = 0
        self.input_mode1_0_len   = 2
        return self.input_mode1_0_value
        
    @input_mode1_0.setter
    def input_mode1_0(self,value):
        self.input_mode1_0_value = value 
        regvalue = self.input_mode1_0
        # perform operation with reg value 
             
class SEQ_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x12
        self.page = 0
        
    @property
    def seq_step_time_cmem1_0(self):
        self.seq_step_time_cmem1_0_pos   = 4
        self.seq_step_time_cmem1_0_len   = 2
        return self.seq_step_time_cmem1_0_value
        
    @seq_step_time_cmem1_0.setter
    def seq_step_time_cmem1_0(self,value):
        self.seq_step_time_cmem1_0_value = value 
        regvalue = self.seq_step_time_cmem1_0
        # perform operation with reg value 
            
    @property
    def seq_step_time_pd1_0(self):
        self.seq_step_time_pd1_0_pos   = 2
        self.seq_step_time_pd1_0_len   = 2
        return self.seq_step_time_pd1_0_value
        
    @seq_step_time_pd1_0.setter
    def seq_step_time_pd1_0(self,value):
        self.seq_step_time_pd1_0_value = value 
        regvalue = self.seq_step_time_pd1_0
        # perform operation with reg value 
            
    @property
    def seq_step_time_pu1_0(self):
        self.seq_step_time_pu1_0_pos   = 0
        self.seq_step_time_pu1_0_len   = 2
        return self.seq_step_time_pu1_0_value
        
    @seq_step_time_pu1_0.setter
    def seq_step_time_pu1_0(self,value):
        self.seq_step_time_pu1_0_value = value 
        regvalue = self.seq_step_time_pu1_0
        # perform operation with reg value 
             
class SEQ_settings_2 :
    
    def __init__(self) -> None:
        self.address = 0x13
        self.page = 0
        
    @property
    def clk_missing_rst_en(self):
        self.clk_missing_rst_en_pos   = 7
        self.clk_missing_rst_en_len   = 1
        return self.clk_missing_rst_en_value
        
    @clk_missing_rst_en.setter
    def clk_missing_rst_en(self,value):
        self.clk_missing_rst_en_value = value 
        regvalue = self.clk_missing_rst_en
        # perform operation with reg value 
            
    @property
    def clk_missing_rst_mode1_0(self):
        self.clk_missing_rst_mode1_0_pos   = 5
        self.clk_missing_rst_mode1_0_len   = 2
        return self.clk_missing_rst_mode1_0_value
        
    @clk_missing_rst_mode1_0.setter
    def clk_missing_rst_mode1_0(self,value):
        self.clk_missing_rst_mode1_0_value = value 
        regvalue = self.clk_missing_rst_mode1_0
        # perform operation with reg value 
            
    @property
    def seq_auto_cal_dis(self):
        self.seq_auto_cal_dis_pos   = 4
        self.seq_auto_cal_dis_len   = 1
        return self.seq_auto_cal_dis_value
        
    @seq_auto_cal_dis.setter
    def seq_auto_cal_dis(self,value):
        self.seq_auto_cal_dis_value = value 
        regvalue = self.seq_auto_cal_dis
        # perform operation with reg value 
            
    @property
    def seq_pd_mode(self):
        self.seq_pd_mode_pos   = 3
        self.seq_pd_mode_len   = 1
        return self.seq_pd_mode_value
        
    @seq_pd_mode.setter
    def seq_pd_mode(self,value):
        self.seq_pd_mode_value = value 
        regvalue = self.seq_pd_mode
        # perform operation with reg value 
            
    @property
    def seq_cmem_wait(self):
        self.seq_cmem_wait_pos   = 1
        self.seq_cmem_wait_len   = 1
        return self.seq_cmem_wait_value
        
    @seq_cmem_wait.setter
    def seq_cmem_wait(self,value):
        self.seq_cmem_wait_value = value 
        regvalue = self.seq_cmem_wait
        # perform operation with reg value 
            
    @property
    def seq_bst_ovp_en(self):
        self.seq_bst_ovp_en_pos   = 0
        self.seq_bst_ovp_en_len   = 1
        return self.seq_bst_ovp_en_value
        
    @seq_bst_ovp_en.setter
    def seq_bst_ovp_en(self,value):
        self.seq_bst_ovp_en_value = value 
        regvalue = self.seq_bst_ovp_en
        # perform operation with reg value 
             
class SEQ_settings_3 :
    
    def __init__(self) -> None:
        self.address = 0x14
        self.page = 0
        
    @property
    def seq_ng_mode(self):
        self.seq_ng_mode_pos   = 3
        self.seq_ng_mode_len   = 1
        return self.seq_ng_mode_value
        
    @seq_ng_mode.setter
    def seq_ng_mode(self,value):
        self.seq_ng_mode_value = value 
        regvalue = self.seq_ng_mode
        # perform operation with reg value 
            
    @property
    def ng_tif_en(self):
        self.ng_tif_en_pos   = 2
        self.ng_tif_en_len   = 1
        return self.ng_tif_en_value
        
    @ng_tif_en.setter
    def ng_tif_en(self,value):
        self.ng_tif_en_value = value 
        regvalue = self.ng_tif_en
        # perform operation with reg value 
            
    @property
    def ng_intfb_pa_en(self):
        self.ng_intfb_pa_en_pos   = 1
        self.ng_intfb_pa_en_len   = 1
        return self.ng_intfb_pa_en_value
        
    @ng_intfb_pa_en.setter
    def ng_intfb_pa_en(self,value):
        self.ng_intfb_pa_en_value = value 
        regvalue = self.ng_intfb_pa_en
        # perform operation with reg value 
            
    @property
    def ng_intfb_clk_en(self):
        self.ng_intfb_clk_en_pos   = 0
        self.ng_intfb_clk_en_len   = 1
        return self.ng_intfb_clk_en_value
        
    @ng_intfb_clk_en.setter
    def ng_intfb_clk_en(self,value):
        self.ng_intfb_clk_en_value = value 
        regvalue = self.ng_intfb_clk_en
        # perform operation with reg value 
             
class SEQ_settings_4 :
    
    def __init__(self) -> None:
        self.address = 0x15
        self.page = 0
        
    @property
    def seq_ramp_offs_step_time10_8(self):
        self.seq_ramp_offs_step_time10_8_pos   = 0
        self.seq_ramp_offs_step_time10_8_len   = 3
        return self.seq_ramp_offs_step_time10_8_value
        
    @seq_ramp_offs_step_time10_8.setter
    def seq_ramp_offs_step_time10_8(self,value):
        self.seq_ramp_offs_step_time10_8_value = value 
        regvalue = self.seq_ramp_offs_step_time10_8
        # perform operation with reg value 
             
class SEQ_settings_5 :
    
    def __init__(self) -> None:
        self.address = 0x16
        self.page = 0
        
    @property
    def seq_ramp_offs_step_time7_0(self):
        self.seq_ramp_offs_step_time7_0_pos   = 0
        self.seq_ramp_offs_step_time7_0_len   = 8
        return self.seq_ramp_offs_step_time7_0_value
        
    @seq_ramp_offs_step_time7_0.setter
    def seq_ramp_offs_step_time7_0(self,value):
        self.seq_ramp_offs_step_time7_0_value = value 
        regvalue = self.seq_ramp_offs_step_time7_0
        # perform operation with reg value 
             
class SEQ_status_register :
    
    def __init__(self) -> None:
        self.address = 0x17
        self.page = 0
        
    @property
    def seq_state4_0(self):
        self.seq_state4_0_pos   = 0
        self.seq_state4_0_len   = 5
        return self.seq_state4_0_value
        
    @seq_state4_0.setter
    def seq_state4_0(self,value):
        self.seq_state4_0_value = value 
        regvalue = self.seq_state4_0
        # perform operation with reg value 
             
class NG_setting :
    
    def __init__(self) -> None:
        self.address = 0x1a
        self.page = 0
        
    @property
    def ng_on(self):
        self.ng_on_pos   = 0
        self.ng_on_len   = 1
        return self.ng_on_value
        
    @ng_on.setter
    def ng_on(self,value):
        self.ng_on_value = value 
        regvalue = self.ng_on
        # perform operation with reg value 
             
class AUTO_mode_setting :
    
    def __init__(self) -> None:
        self.address = 0x1b
        self.page = 0
        
    @property
    def auto_mode_en(self):
        self.auto_mode_en_pos   = 0
        self.auto_mode_en_len   = 1
        return self.auto_mode_en_value
        
    @auto_mode_en.setter
    def auto_mode_en(self,value):
        self.auto_mode_en_value = value 
        regvalue = self.auto_mode_en
        # perform operation with reg value 
             
class SEQ_low_power_mode :
    
    def __init__(self) -> None:
        self.address = 0x1c
        self.page = 0
        
    @property
    def force_et_seq_clock_on(self):
        self.force_et_seq_clock_on_pos   = 0
        self.force_et_seq_clock_on_len   = 1
        return self.force_et_seq_clock_on_value
        
    @force_et_seq_clock_on.setter
    def force_et_seq_clock_on(self,value):
        self.force_et_seq_clock_on_value = value 
        regvalue = self.force_et_seq_clock_on
        # perform operation with reg value 
             
class PDM_low_freq_reg :
    
    def __init__(self) -> None:
        self.address = 0x1d
        self.page = 0
        
    @property
    def pdm_mode_low_freq(self):
        self.pdm_mode_low_freq_pos   = 0
        self.pdm_mode_low_freq_len   = 1
        return self.pdm_mode_low_freq_value
        
    @pdm_mode_low_freq.setter
    def pdm_mode_low_freq(self,value):
        self.pdm_mode_low_freq_value = value 
        regvalue = self.pdm_mode_low_freq
        # perform operation with reg value 
             
class ANA_SPARE_Register :
    
    def __init__(self) -> None:
        self.address = 0x20
        self.page = 0
        
    @property
    def ana_spare23_0(self):
        self.ana_spare23_0_pos   = 4
        self.ana_spare23_0_len   = 4
        return self.ana_spare23_0_value
        
    @ana_spare23_0.setter
    def ana_spare23_0(self,value):
        self.ana_spare23_0_value = value 
        regvalue = self.ana_spare23_0
        # perform operation with reg value 
            
    @property
    def ana_spare13_0(self):
        self.ana_spare13_0_pos   = 0
        self.ana_spare13_0_len   = 4
        return self.ana_spare13_0_value
        
    @ana_spare13_0.setter
    def ana_spare13_0(self,value):
        self.ana_spare13_0_value = value 
        regvalue = self.ana_spare13_0
        # perform operation with reg value 
             
class TDM_apply_configuration :
    
    def __init__(self) -> None:
        self.address = 0x30
        self.page = 0
        
    @property
    def tdm_resync(self):
        self.tdm_resync_pos   = 7
        self.tdm_resync_len   = 1
        return self.tdm_resync_value
        
    @tdm_resync.setter
    def tdm_resync(self,value):
        self.tdm_resync_value = value 
        regvalue = self.tdm_resync
        # perform operation with reg value 
             
class TDM_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x31
        self.page = 0
        
    @property
    def tdm_delay_mode(self):
        self.tdm_delay_mode_pos   = 2
        self.tdm_delay_mode_len   = 1
        return self.tdm_delay_mode_value
        
    @tdm_delay_mode.setter
    def tdm_delay_mode(self,value):
        self.tdm_delay_mode_value = value 
        regvalue = self.tdm_delay_mode
        # perform operation with reg value 
            
    @property
    def tdm_fsyn_polarity(self):
        self.tdm_fsyn_polarity_pos   = 1
        self.tdm_fsyn_polarity_len   = 1
        return self.tdm_fsyn_polarity_value
        
    @tdm_fsyn_polarity.setter
    def tdm_fsyn_polarity(self,value):
        self.tdm_fsyn_polarity_value = value 
        regvalue = self.tdm_fsyn_polarity
        # perform operation with reg value 
            
    @property
    def tdm_bclk_polarity(self):
        self.tdm_bclk_polarity_pos   = 0
        self.tdm_bclk_polarity_len   = 1
        return self.tdm_bclk_polarity_value
        
    @tdm_bclk_polarity.setter
    def tdm_bclk_polarity(self,value):
        self.tdm_bclk_polarity_value = value 
        regvalue = self.tdm_bclk_polarity
        # perform operation with reg value 
             
class TDM_settings_2 :
    
    def __init__(self) -> None:
        self.address = 0x32
        self.page = 0
        
    @property
    def tdm_fsyn_rate2_0(self):
        self.tdm_fsyn_rate2_0_pos   = 4
        self.tdm_fsyn_rate2_0_len   = 3
        return self.tdm_fsyn_rate2_0_value
        
    @tdm_fsyn_rate2_0.setter
    def tdm_fsyn_rate2_0(self,value):
        self.tdm_fsyn_rate2_0_value = value 
        regvalue = self.tdm_fsyn_rate2_0
        # perform operation with reg value 
            
    @property
    def tdm_bclk_osr2_0(self):
        self.tdm_bclk_osr2_0_pos   = 0
        self.tdm_bclk_osr2_0_len   = 3
        return self.tdm_bclk_osr2_0_value
        
    @tdm_bclk_osr2_0.setter
    def tdm_bclk_osr2_0(self,value):
        self.tdm_bclk_osr2_0_value = value 
        regvalue = self.tdm_bclk_osr2_0
        # perform operation with reg value 
             
class TDM_settings_3 :
    
    def __init__(self) -> None:
        self.address = 0x33
        self.page = 0
        
    @property
    def tdm_i_skip_bclk5_0(self):
        self.tdm_i_skip_bclk5_0_pos   = 0
        self.tdm_i_skip_bclk5_0_len   = 6
        return self.tdm_i_skip_bclk5_0_value
        
    @tdm_i_skip_bclk5_0.setter
    def tdm_i_skip_bclk5_0(self,value):
        self.tdm_i_skip_bclk5_0_value = value 
        regvalue = self.tdm_i_skip_bclk5_0
        # perform operation with reg value 
             
class TDM_settings_4 :
    
    def __init__(self) -> None:
        self.address = 0x35
        self.page = 0
        
    @property
    def tdm_i_slot_size1_0(self):
        self.tdm_i_slot_size1_0_pos   = 6
        self.tdm_i_slot_size1_0_len   = 2
        return self.tdm_i_slot_size1_0_value
        
    @tdm_i_slot_size1_0.setter
    def tdm_i_slot_size1_0(self,value):
        self.tdm_i_slot_size1_0_value = value 
        regvalue = self.tdm_i_slot_size1_0
        # perform operation with reg value 
            
    @property
    def tdm_ch1i_dl(self):
        self.tdm_ch1i_dl_pos   = 5
        self.tdm_ch1i_dl_len   = 1
        return self.tdm_ch1i_dl_value
        
    @tdm_ch1i_dl.setter
    def tdm_ch1i_dl(self,value):
        self.tdm_ch1i_dl_value = value 
        regvalue = self.tdm_ch1i_dl
        # perform operation with reg value 
            
    @property
    def tdm_ch1i_slot4_0(self):
        self.tdm_ch1i_slot4_0_pos   = 0
        self.tdm_ch1i_slot4_0_len   = 5
        return self.tdm_ch1i_slot4_0_value
        
    @tdm_ch1i_slot4_0.setter
    def tdm_ch1i_slot4_0(self,value):
        self.tdm_ch1i_slot4_0_value = value 
        regvalue = self.tdm_ch1i_slot4_0
        # perform operation with reg value 
             
class Clock_monitor_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x39
        self.page = 0
        
    @property
    def tdm_fsyn_rate_mnt_en(self):
        self.tdm_fsyn_rate_mnt_en_pos   = 7
        self.tdm_fsyn_rate_mnt_en_len   = 1
        return self.tdm_fsyn_rate_mnt_en_value
        
    @tdm_fsyn_rate_mnt_en.setter
    def tdm_fsyn_rate_mnt_en(self,value):
        self.tdm_fsyn_rate_mnt_en_value = value 
        regvalue = self.tdm_fsyn_rate_mnt_en
        # perform operation with reg value 
            
    @property
    def tdm_fsyn_mnt_en(self):
        self.tdm_fsyn_mnt_en_pos   = 6
        self.tdm_fsyn_mnt_en_len   = 1
        return self.tdm_fsyn_mnt_en_value
        
    @tdm_fsyn_mnt_en.setter
    def tdm_fsyn_mnt_en(self,value):
        self.tdm_fsyn_mnt_en_value = value 
        regvalue = self.tdm_fsyn_mnt_en
        # perform operation with reg value 
            
    @property
    def tdm_fsyn_mnt_mode1_0(self):
        self.tdm_fsyn_mnt_mode1_0_pos   = 4
        self.tdm_fsyn_mnt_mode1_0_len   = 2
        return self.tdm_fsyn_mnt_mode1_0_value
        
    @tdm_fsyn_mnt_mode1_0.setter
    def tdm_fsyn_mnt_mode1_0(self,value):
        self.tdm_fsyn_mnt_mode1_0_value = value 
        regvalue = self.tdm_fsyn_mnt_mode1_0
        # perform operation with reg value 
            
    @property
    def tdm_fsyn_mnt_mask_cnt3_0(self):
        self.tdm_fsyn_mnt_mask_cnt3_0_pos   = 0
        self.tdm_fsyn_mnt_mask_cnt3_0_len   = 4
        return self.tdm_fsyn_mnt_mask_cnt3_0_value
        
    @tdm_fsyn_mnt_mask_cnt3_0.setter
    def tdm_fsyn_mnt_mask_cnt3_0(self,value):
        self.tdm_fsyn_mnt_mask_cnt3_0_value = value 
        regvalue = self.tdm_fsyn_mnt_mask_cnt3_0
        # perform operation with reg value 
             
class Clock_monitor_settings_2 :
    
    def __init__(self) -> None:
        self.address = 0x3a
        self.page = 0
        
    @property
    def tdm_sync_mode(self):
        self.tdm_sync_mode_pos   = 2
        self.tdm_sync_mode_len   = 1
        return self.tdm_sync_mode_value
        
    @tdm_sync_mode.setter
    def tdm_sync_mode(self,value):
        self.tdm_sync_mode_value = value 
        regvalue = self.tdm_sync_mode
        # perform operation with reg value 
            
    @property
    def tdm_bclk_mnt_mode(self):
        self.tdm_bclk_mnt_mode_pos   = 1
        self.tdm_bclk_mnt_mode_len   = 1
        return self.tdm_bclk_mnt_mode_value
        
    @tdm_bclk_mnt_mode.setter
    def tdm_bclk_mnt_mode(self,value):
        self.tdm_bclk_mnt_mode_value = value 
        regvalue = self.tdm_bclk_mnt_mode
        # perform operation with reg value 
            
    @property
    def tdm_auto_fsyn_rate(self):
        self.tdm_auto_fsyn_rate_pos   = 0
        self.tdm_auto_fsyn_rate_len   = 1
        return self.tdm_auto_fsyn_rate_value
        
    @tdm_auto_fsyn_rate.setter
    def tdm_auto_fsyn_rate(self,value):
        self.tdm_auto_fsyn_rate_value = value 
        regvalue = self.tdm_auto_fsyn_rate
        # perform operation with reg value 
             
class TIF_register :
    
    def __init__(self) -> None:
        self.address = 0x3b
        self.page = 0
        
    @property
    def fir1_m2db(self):
        self.fir1_m2db_pos   = 0
        self.fir1_m2db_len   = 1
        return self.fir1_m2db_value
        
    @fir1_m2db.setter
    def fir1_m2db(self,value):
        self.fir1_m2db_value = value 
        regvalue = self.fir1_m2db
        # perform operation with reg value 
             
class TIF_Spare_Register :
    
    def __init__(self) -> None:
        self.address = 0x3f
        self.page = 0
        
    @property
    def tif_spare7_0(self):
        self.tif_spare7_0_pos   = 0
        self.tif_spare7_0_len   = 8
        return self.tif_spare7_0_value
        
    @tif_spare7_0.setter
    def tif_spare7_0(self,value):
        self.tif_spare7_0_value = value 
        regvalue = self.tif_spare7_0
        # perform operation with reg value 
             
class NGIF_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x50
        self.page = 0
        
    @property
    def ngif_filt_ratio1_0(self):
        self.ngif_filt_ratio1_0_pos   = 6
        self.ngif_filt_ratio1_0_len   = 2
        return self.ngif_filt_ratio1_0_value
        
    @ngif_filt_ratio1_0.setter
    def ngif_filt_ratio1_0(self,value):
        self.ngif_filt_ratio1_0_value = value 
        regvalue = self.ngif_filt_ratio1_0
        # perform operation with reg value 
            
    @property
    def ngif_filt_sample1_0(self):
        self.ngif_filt_sample1_0_pos   = 4
        self.ngif_filt_sample1_0_len   = 2
        return self.ngif_filt_sample1_0_value
        
    @ngif_filt_sample1_0.setter
    def ngif_filt_sample1_0(self,value):
        self.ngif_filt_sample1_0_value = value 
        regvalue = self.ngif_filt_sample1_0
        # perform operation with reg value 
            
    @property
    def ngif_hyst_en(self):
        self.ngif_hyst_en_pos   = 3
        self.ngif_hyst_en_len   = 1
        return self.ngif_hyst_en_value
        
    @ngif_hyst_en.setter
    def ngif_hyst_en(self,value):
        self.ngif_hyst_en_value = value 
        regvalue = self.ngif_hyst_en
        # perform operation with reg value 
            
    @property
    def ngif_mask(self):
        self.ngif_mask_pos   = 1
        self.ngif_mask_len   = 1
        return self.ngif_mask_value
        
    @ngif_mask.setter
    def ngif_mask(self,value):
        self.ngif_mask_value = value 
        regvalue = self.ngif_mask
        # perform operation with reg value 
            
    @property
    def ngif_en(self):
        self.ngif_en_pos   = 0
        self.ngif_en_len   = 1
        return self.ngif_en_value
        
    @ngif_en.setter
    def ngif_en(self,value):
        self.ngif_en_value = value 
        regvalue = self.ngif_en
        # perform operation with reg value 
             
class NGIF_settings_2 :
    
    def __init__(self) -> None:
        self.address = 0x51
        self.page = 0
        
    @property
    def ngif_thresh12_8(self):
        self.ngif_thresh12_8_pos   = 0
        self.ngif_thresh12_8_len   = 5
        return self.ngif_thresh12_8_value
        
    @ngif_thresh12_8.setter
    def ngif_thresh12_8(self,value):
        self.ngif_thresh12_8_value = value 
        regvalue = self.ngif_thresh12_8
        # perform operation with reg value 
             
class NGIF_settings_3 :
    
    def __init__(self) -> None:
        self.address = 0x52
        self.page = 0
        
    @property
    def ngif_thresh7_0(self):
        self.ngif_thresh7_0_pos   = 0
        self.ngif_thresh7_0_len   = 8
        return self.ngif_thresh7_0_value
        
    @ngif_thresh7_0.setter
    def ngif_thresh7_0(self,value):
        self.ngif_thresh7_0_value = value 
        regvalue = self.ngif_thresh7_0
        # perform operation with reg value 
             
class SDM_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0x70
        self.page = 0
        
    @property
    def sdm1_order(self):
        self.sdm1_order_pos   = 7
        self.sdm1_order_len   = 1
        return self.sdm1_order_value
        
    @sdm1_order.setter
    def sdm1_order(self,value):
        self.sdm1_order_value = value 
        regvalue = self.sdm1_order
        # perform operation with reg value 
            
    @property
    def sdm1_dith_type(self):
        self.sdm1_dith_type_pos   = 6
        self.sdm1_dith_type_len   = 1
        return self.sdm1_dith_type_value
        
    @sdm1_dith_type.setter
    def sdm1_dith_type(self,value):
        self.sdm1_dith_type_value = value 
        regvalue = self.sdm1_dith_type
        # perform operation with reg value 
            
    @property
    def sdm1_dith_div1_0(self):
        self.sdm1_dith_div1_0_pos   = 4
        self.sdm1_dith_div1_0_len   = 2
        return self.sdm1_dith_div1_0_value
        
    @sdm1_dith_div1_0.setter
    def sdm1_dith_div1_0(self,value):
        self.sdm1_dith_div1_0_value = value 
        regvalue = self.sdm1_dith_div1_0
        # perform operation with reg value 
            
    @property
    def sdm1_dith_strength3_0(self):
        self.sdm1_dith_strength3_0_pos   = 0
        self.sdm1_dith_strength3_0_len   = 4
        return self.sdm1_dith_strength3_0_value
        
    @sdm1_dith_strength3_0.setter
    def sdm1_dith_strength3_0(self,value):
        self.sdm1_dith_strength3_0_value = value 
        regvalue = self.sdm1_dith_strength3_0
        # perform operation with reg value 
             
class SDM_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0x71
        self.page = 0
        
    @property
    def sdm2_order(self):
        self.sdm2_order_pos   = 7
        self.sdm2_order_len   = 1
        return self.sdm2_order_value
        
    @sdm2_order.setter
    def sdm2_order(self,value):
        self.sdm2_order_value = value 
        regvalue = self.sdm2_order
        # perform operation with reg value 
            
    @property
    def sdm2_dith_type(self):
        self.sdm2_dith_type_pos   = 6
        self.sdm2_dith_type_len   = 1
        return self.sdm2_dith_type_value
        
    @sdm2_dith_type.setter
    def sdm2_dith_type(self,value):
        self.sdm2_dith_type_value = value 
        regvalue = self.sdm2_dith_type
        # perform operation with reg value 
            
    @property
    def sdm2_dith_div1_0(self):
        self.sdm2_dith_div1_0_pos   = 4
        self.sdm2_dith_div1_0_len   = 2
        return self.sdm2_dith_div1_0_value
        
    @sdm2_dith_div1_0.setter
    def sdm2_dith_div1_0(self,value):
        self.sdm2_dith_div1_0_value = value 
        regvalue = self.sdm2_dith_div1_0
        # perform operation with reg value 
            
    @property
    def sdm2_dith_strength3_0(self):
        self.sdm2_dith_strength3_0_pos   = 0
        self.sdm2_dith_strength3_0_len   = 4
        return self.sdm2_dith_strength3_0_value
        
    @sdm2_dith_strength3_0.setter
    def sdm2_dith_strength3_0(self,value):
        self.sdm2_dith_strength3_0_value = value 
        regvalue = self.sdm2_dith_strength3_0
        # perform operation with reg value 
             
class SDM_Register_3 :
    
    def __init__(self) -> None:
        self.address = 0x72
        self.page = 0
        
    @property
    def sdm3_order(self):
        self.sdm3_order_pos   = 7
        self.sdm3_order_len   = 1
        return self.sdm3_order_value
        
    @sdm3_order.setter
    def sdm3_order(self,value):
        self.sdm3_order_value = value 
        regvalue = self.sdm3_order
        # perform operation with reg value 
            
    @property
    def sdm3_dith_type(self):
        self.sdm3_dith_type_pos   = 6
        self.sdm3_dith_type_len   = 1
        return self.sdm3_dith_type_value
        
    @sdm3_dith_type.setter
    def sdm3_dith_type(self,value):
        self.sdm3_dith_type_value = value 
        regvalue = self.sdm3_dith_type
        # perform operation with reg value 
            
    @property
    def sdm3_dith_div1_0(self):
        self.sdm3_dith_div1_0_pos   = 4
        self.sdm3_dith_div1_0_len   = 2
        return self.sdm3_dith_div1_0_value
        
    @sdm3_dith_div1_0.setter
    def sdm3_dith_div1_0(self,value):
        self.sdm3_dith_div1_0_value = value 
        regvalue = self.sdm3_dith_div1_0
        # perform operation with reg value 
            
    @property
    def sdm3_dith_strength3_0(self):
        self.sdm3_dith_strength3_0_pos   = 0
        self.sdm3_dith_strength3_0_len   = 4
        return self.sdm3_dith_strength3_0_value
        
    @sdm3_dith_strength3_0.setter
    def sdm3_dith_strength3_0(self,value):
        self.sdm3_dith_strength3_0_value = value 
        regvalue = self.sdm3_dith_strength3_0
        # perform operation with reg value 
             
class DWA_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0x75
        self.page = 0
        
    @property
    def dwa1_freq_sel1_0(self):
        self.dwa1_freq_sel1_0_pos   = 6
        self.dwa1_freq_sel1_0_len   = 2
        return self.dwa1_freq_sel1_0_value
        
    @dwa1_freq_sel1_0.setter
    def dwa1_freq_sel1_0(self,value):
        self.dwa1_freq_sel1_0_value = value 
        regvalue = self.dwa1_freq_sel1_0
        # perform operation with reg value 
            
    @property
    def dwa1_level1_0(self):
        self.dwa1_level1_0_pos   = 4
        self.dwa1_level1_0_len   = 2
        return self.dwa1_level1_0_value
        
    @dwa1_level1_0.setter
    def dwa1_level1_0(self,value):
        self.dwa1_level1_0_value = value 
        regvalue = self.dwa1_level1_0
        # perform operation with reg value 
            
    @property
    def dac_forcez3(self):
        self.dac_forcez3_pos   = 3
        self.dac_forcez3_len   = 1
        return self.dac_forcez3_value
        
    @dac_forcez3.setter
    def dac_forcez3(self,value):
        self.dac_forcez3_value = value 
        regvalue = self.dac_forcez3
        # perform operation with reg value 
            
    @property
    def dac_forcez2(self):
        self.dac_forcez2_pos   = 2
        self.dac_forcez2_len   = 1
        return self.dac_forcez2_value
        
    @dac_forcez2.setter
    def dac_forcez2(self,value):
        self.dac_forcez2_value = value 
        regvalue = self.dac_forcez2
        # perform operation with reg value 
            
    @property
    def dac_forcez1(self):
        self.dac_forcez1_pos   = 1
        self.dac_forcez1_len   = 1
        return self.dac_forcez1_value
        
    @dac_forcez1.setter
    def dac_forcez1(self,value):
        self.dac_forcez1_value = value 
        regvalue = self.dac_forcez1
        # perform operation with reg value 
            
    @property
    def dac_inv_dwa_data(self):
        self.dac_inv_dwa_data_pos   = 0
        self.dac_inv_dwa_data_len   = 1
        return self.dac_inv_dwa_data_value
        
    @dac_inv_dwa_data.setter
    def dac_inv_dwa_data(self,value):
        self.dac_inv_dwa_data_value = value 
        regvalue = self.dac_inv_dwa_data
        # perform operation with reg value 
             
class DWA_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0x76
        self.page = 0
        
    @property
    def dwa3_freq_sel1_0(self):
        self.dwa3_freq_sel1_0_pos   = 6
        self.dwa3_freq_sel1_0_len   = 2
        return self.dwa3_freq_sel1_0_value
        
    @dwa3_freq_sel1_0.setter
    def dwa3_freq_sel1_0(self,value):
        self.dwa3_freq_sel1_0_value = value 
        regvalue = self.dwa3_freq_sel1_0
        # perform operation with reg value 
            
    @property
    def dwa3_level1_0(self):
        self.dwa3_level1_0_pos   = 4
        self.dwa3_level1_0_len   = 2
        return self.dwa3_level1_0_value
        
    @dwa3_level1_0.setter
    def dwa3_level1_0(self,value):
        self.dwa3_level1_0_value = value 
        regvalue = self.dwa3_level1_0
        # perform operation with reg value 
            
    @property
    def dwa2_freq_sel1_0(self):
        self.dwa2_freq_sel1_0_pos   = 2
        self.dwa2_freq_sel1_0_len   = 2
        return self.dwa2_freq_sel1_0_value
        
    @dwa2_freq_sel1_0.setter
    def dwa2_freq_sel1_0(self,value):
        self.dwa2_freq_sel1_0_value = value 
        regvalue = self.dwa2_freq_sel1_0
        # perform operation with reg value 
            
    @property
    def dwa2_level1_0(self):
        self.dwa2_level1_0_pos   = 0
        self.dwa2_level1_0_len   = 2
        return self.dwa2_level1_0_value
        
    @dwa2_level1_0.setter
    def dwa2_level1_0(self,value):
        self.dwa2_level1_0_value = value 
        regvalue = self.dwa2_level1_0
        # perform operation with reg value 
             
class DWA_Register_3 :
    
    def __init__(self) -> None:
        self.address = 0x77
        self.page = 0
        
    @property
    def dwa1_mode1_0(self):
        self.dwa1_mode1_0_pos   = 6
        self.dwa1_mode1_0_len   = 2
        return self.dwa1_mode1_0_value
        
    @dwa1_mode1_0.setter
    def dwa1_mode1_0(self,value):
        self.dwa1_mode1_0_value = value 
        regvalue = self.dwa1_mode1_0
        # perform operation with reg value 
            
    @property
    def dwa1_shift_sel4_0(self):
        self.dwa1_shift_sel4_0_pos   = 0
        self.dwa1_shift_sel4_0_len   = 5
        return self.dwa1_shift_sel4_0_value
        
    @dwa1_shift_sel4_0.setter
    def dwa1_shift_sel4_0(self,value):
        self.dwa1_shift_sel4_0_value = value 
        regvalue = self.dwa1_shift_sel4_0
        # perform operation with reg value 
             
class DWA_Register_4 :
    
    def __init__(self) -> None:
        self.address = 0x78
        self.page = 0
        
    @property
    def dwa2_mode1_0(self):
        self.dwa2_mode1_0_pos   = 6
        self.dwa2_mode1_0_len   = 2
        return self.dwa2_mode1_0_value
        
    @dwa2_mode1_0.setter
    def dwa2_mode1_0(self,value):
        self.dwa2_mode1_0_value = value 
        regvalue = self.dwa2_mode1_0
        # perform operation with reg value 
            
    @property
    def dwa2_shift_sel4_0(self):
        self.dwa2_shift_sel4_0_pos   = 0
        self.dwa2_shift_sel4_0_len   = 5
        return self.dwa2_shift_sel4_0_value
        
    @dwa2_shift_sel4_0.setter
    def dwa2_shift_sel4_0(self,value):
        self.dwa2_shift_sel4_0_value = value 
        regvalue = self.dwa2_shift_sel4_0
        # perform operation with reg value 
             
class DWA_Register_5 :
    
    def __init__(self) -> None:
        self.address = 0x79
        self.page = 0
        
    @property
    def dwa3_mode1_0(self):
        self.dwa3_mode1_0_pos   = 6
        self.dwa3_mode1_0_len   = 2
        return self.dwa3_mode1_0_value
        
    @dwa3_mode1_0.setter
    def dwa3_mode1_0(self,value):
        self.dwa3_mode1_0_value = value 
        regvalue = self.dwa3_mode1_0
        # perform operation with reg value 
            
    @property
    def dwa3_shift_sel5_0(self):
        self.dwa3_shift_sel5_0_pos   = 0
        self.dwa3_shift_sel5_0_len   = 6
        return self.dwa3_shift_sel5_0_value
        
    @dwa3_shift_sel5_0.setter
    def dwa3_shift_sel5_0(self,value):
        self.dwa3_shift_sel5_0_value = value 
        regvalue = self.dwa3_shift_sel5_0
        # perform operation with reg value 
             
class DYC_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0x7a
        self.page = 0
        
    @property
    def dac1_dyc_en(self):
        self.dac1_dyc_en_pos   = 7
        self.dac1_dyc_en_len   = 1
        return self.dac1_dyc_en_value
        
    @dac1_dyc_en.setter
    def dac1_dyc_en(self,value):
        self.dac1_dyc_en_value = value 
        regvalue = self.dac1_dyc_en
        # perform operation with reg value 
            
    @property
    def dac1_dyc_target5_0(self):
        self.dac1_dyc_target5_0_pos   = 0
        self.dac1_dyc_target5_0_len   = 6
        return self.dac1_dyc_target5_0_value
        
    @dac1_dyc_target5_0.setter
    def dac1_dyc_target5_0(self,value):
        self.dac1_dyc_target5_0_value = value 
        regvalue = self.dac1_dyc_target5_0
        # perform operation with reg value 
             
class DYC_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0x7b
        self.page = 0
        
    @property
    def dac2_dyc_en(self):
        self.dac2_dyc_en_pos   = 7
        self.dac2_dyc_en_len   = 1
        return self.dac2_dyc_en_value
        
    @dac2_dyc_en.setter
    def dac2_dyc_en(self,value):
        self.dac2_dyc_en_value = value 
        regvalue = self.dac2_dyc_en
        # perform operation with reg value 
            
    @property
    def dac2_dyc_target5_0(self):
        self.dac2_dyc_target5_0_pos   = 0
        self.dac2_dyc_target5_0_len   = 6
        return self.dac2_dyc_target5_0_value
        
    @dac2_dyc_target5_0.setter
    def dac2_dyc_target5_0(self,value):
        self.dac2_dyc_target5_0_value = value 
        regvalue = self.dac2_dyc_target5_0
        # perform operation with reg value 
             
class DYC_Register_3 :
    
    def __init__(self) -> None:
        self.address = 0x7c
        self.page = 0
        
    @property
    def dac3_dyc_en(self):
        self.dac3_dyc_en_pos   = 7
        self.dac3_dyc_en_len   = 1
        return self.dac3_dyc_en_value
        
    @dac3_dyc_en.setter
    def dac3_dyc_en(self,value):
        self.dac3_dyc_en_value = value 
        regvalue = self.dac3_dyc_en
        # perform operation with reg value 
            
    @property
    def dac3_dyc_target5_0(self):
        self.dac3_dyc_target5_0_pos   = 0
        self.dac3_dyc_target5_0_len   = 6
        return self.dac3_dyc_target5_0_value
        
    @dac3_dyc_target5_0.setter
    def dac3_dyc_target5_0(self,value):
        self.dac3_dyc_target5_0_value = value 
        regvalue = self.dac3_dyc_target5_0
        # perform operation with reg value 
             
class MOD_Spare_Register :
    
    def __init__(self) -> None:
        self.address = 0x7f
        self.page = 0
        
    @property
    def mod_spare7_0(self):
        self.mod_spare7_0_pos   = 0
        self.mod_spare7_0_len   = 8
        return self.mod_spare7_0_value
        
    @mod_spare7_0.setter
    def mod_spare7_0(self,value):
        self.mod_spare7_0_value = value 
        regvalue = self.mod_spare7_0
        # perform operation with reg value 
             
class REF_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0x80
        self.page = 0
        
    @property
    def pa_zsel3_0(self):
        self.pa_zsel3_0_pos   = 4
        self.pa_zsel3_0_len   = 4
        return self.pa_zsel3_0_value
        
    @pa_zsel3_0.setter
    def pa_zsel3_0(self,value):
        self.pa_zsel3_0_value = value 
        regvalue = self.pa_zsel3_0
        # perform operation with reg value 
            
    @property
    def tsd_pa_down_en(self):
        self.tsd_pa_down_en_pos   = 3
        self.tsd_pa_down_en_len   = 1
        return self.tsd_pa_down_en_value
        
    @tsd_pa_down_en.setter
    def tsd_pa_down_en(self,value):
        self.tsd_pa_down_en_value = value 
        regvalue = self.tsd_pa_down_en
        # perform operation with reg value 
            
    @property
    def ref_dvddldo_mode(self):
        self.ref_dvddldo_mode_pos   = 2
        self.ref_dvddldo_mode_len   = 1
        return self.ref_dvddldo_mode_value
        
    @ref_dvddldo_mode.setter
    def ref_dvddldo_mode(self,value):
        self.ref_dvddldo_mode_value = value 
        regvalue = self.ref_dvddldo_mode
        # perform operation with reg value 
            
    @property
    def tsd_temp_sel1_0(self):
        self.tsd_temp_sel1_0_pos   = 0
        self.tsd_temp_sel1_0_len   = 2
        return self.tsd_temp_sel1_0_value
        
    @tsd_temp_sel1_0.setter
    def tsd_temp_sel1_0(self,value):
        self.tsd_temp_sel1_0_value = value 
        regvalue = self.tsd_temp_sel1_0
        # perform operation with reg value 
             
class REF_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0x81
        self.page = 0
        
    @property
    def rfu_tsd_temp_sel1_0(self):
        self.rfu_tsd_temp_sel1_0_pos   = 0
        self.rfu_tsd_temp_sel1_0_len   = 2
        return self.rfu_tsd_temp_sel1_0_value
        
    @rfu_tsd_temp_sel1_0.setter
    def rfu_tsd_temp_sel1_0(self,value):
        self.rfu_tsd_temp_sel1_0_value = value 
        regvalue = self.rfu_tsd_temp_sel1_0
        # perform operation with reg value 
             
class ANA_gain_Register :
    
    def __init__(self) -> None:
        self.address = 0x83
        self.page = 0
        
    @property
    def dpa_ana_gain2_0(self):
        self.dpa_ana_gain2_0_pos   = 0
        self.dpa_ana_gain2_0_len   = 3
        return self.dpa_ana_gain2_0_value
        
    @dpa_ana_gain2_0.setter
    def dpa_ana_gain2_0(self,value):
        self.dpa_ana_gain2_0_value = value 
        regvalue = self.dpa_ana_gain2_0
        # perform operation with reg value 
             
class Protection_reg_1 :
    
    def __init__(self) -> None:
        self.address = 0x84
        self.page = 0
        
    @property
    def bst_fault(self):
        self.bst_fault_pos   = 7
        self.bst_fault_len   = 1
        return self.bst_fault_value
        
    @bst_fault.setter
    def bst_fault(self,value):
        self.bst_fault_value = value 
        regvalue = self.bst_fault
        # perform operation with reg value 
            
    @property
    def seq_pwrok_mode2_0(self):
        self.seq_pwrok_mode2_0_pos   = 4
        self.seq_pwrok_mode2_0_len   = 3
        return self.seq_pwrok_mode2_0_value
        
    @seq_pwrok_mode2_0.setter
    def seq_pwrok_mode2_0(self,value):
        self.seq_pwrok_mode2_0_value = value 
        regvalue = self.seq_pwrok_mode2_0
        # perform operation with reg value 
            
    @property
    def seq_pwrok_deglitch_range(self):
        self.seq_pwrok_deglitch_range_pos   = 0
        self.seq_pwrok_deglitch_range_len   = 1
        return self.seq_pwrok_deglitch_range_value
        
    @seq_pwrok_deglitch_range.setter
    def seq_pwrok_deglitch_range(self,value):
        self.seq_pwrok_deglitch_range_value = value 
        regvalue = self.seq_pwrok_deglitch_range
        # perform operation with reg value 
             
class Protection_reg_2 :
    
    def __init__(self) -> None:
        self.address = 0x85
        self.page = 0
        
    @property
    def seq_pwrok_deglitch_time7_0(self):
        self.seq_pwrok_deglitch_time7_0_pos   = 0
        self.seq_pwrok_deglitch_time7_0_len   = 8
        return self.seq_pwrok_deglitch_time7_0_value
        
    @seq_pwrok_deglitch_time7_0.setter
    def seq_pwrok_deglitch_time7_0(self,value):
        self.seq_pwrok_deglitch_time7_0_value = value 
        regvalue = self.seq_pwrok_deglitch_time7_0
        # perform operation with reg value 
             
class Protection_reg_3 :
    
    def __init__(self) -> None:
        self.address = 0x86
        self.page = 0
        
    @property
    def pa_rsk(self):
        self.pa_rsk_pos   = 3
        self.pa_rsk_len   = 1
        return self.pa_rsk_value
        
    @pa_rsk.setter
    def pa_rsk(self,value):
        self.pa_rsk_value = value 
        regvalue = self.pa_rsk
        # perform operation with reg value 
            
    @property
    def pa_r300k_comp_dis(self):
        self.pa_r300k_comp_dis_pos   = 2
        self.pa_r300k_comp_dis_len   = 1
        return self.pa_r300k_comp_dis_value
        
    @pa_r300k_comp_dis.setter
    def pa_r300k_comp_dis(self,value):
        self.pa_r300k_comp_dis_value = value 
        regvalue = self.pa_r300k_comp_dis
        # perform operation with reg value 
            
    @property
    def pa_lp_en(self):
        self.pa_lp_en_pos   = 1
        self.pa_lp_en_len   = 1
        return self.pa_lp_en_value
        
    @pa_lp_en.setter
    def pa_lp_en(self,value):
        self.pa_lp_en_value = value 
        regvalue = self.pa_lp_en
        # perform operation with reg value 
            
    @property
    def pa_ocp_en(self):
        self.pa_ocp_en_pos   = 0
        self.pa_ocp_en_len   = 1
        return self.pa_ocp_en_value
        
    @pa_ocp_en.setter
    def pa_ocp_en(self,value):
        self.pa_ocp_en_value = value 
        regvalue = self.pa_ocp_en
        # perform operation with reg value 
             
class Protection_reg_4 :
    
    def __init__(self) -> None:
        self.address = 0x87
        self.page = 0
        
    @property
    def pa_clamp_th4_0(self):
        self.pa_clamp_th4_0_pos   = 0
        self.pa_clamp_th4_0_len   = 5
        return self.pa_clamp_th4_0_value
        
    @pa_clamp_th4_0.setter
    def pa_clamp_th4_0(self,value):
        self.pa_clamp_th4_0_value = value 
        regvalue = self.pa_clamp_th4_0
        # perform operation with reg value 
             
class Protection_reg_5 :
    
    def __init__(self) -> None:
        self.address = 0x88
        self.page = 0
        
    @property
    def pa_nmos_clamp_th4_0(self):
        self.pa_nmos_clamp_th4_0_pos   = 0
        self.pa_nmos_clamp_th4_0_len   = 5
        return self.pa_nmos_clamp_th4_0_value
        
    @pa_nmos_clamp_th4_0.setter
    def pa_nmos_clamp_th4_0(self,value):
        self.pa_nmos_clamp_th4_0_value = value 
        regvalue = self.pa_nmos_clamp_th4_0
        # perform operation with reg value 
             
class SEQ_Spare_Register :
    
    def __init__(self) -> None:
        self.address = 0x8f
        self.page = 0
        
    @property
    def seq_spare7_0(self):
        self.seq_spare7_0_pos   = 0
        self.seq_spare7_0_len   = 8
        return self.seq_spare7_0_value
        
    @seq_spare7_0.setter
    def seq_spare7_0(self,value):
        self.seq_spare7_0_value = value 
        regvalue = self.seq_spare7_0
        # perform operation with reg value 
             
class BST_Comp_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0xb0
        self.page = 0
        
    @property
    def bst_byp_en(self):
        self.bst_byp_en_pos   = 7
        self.bst_byp_en_len   = 1
        return self.bst_byp_en_value
        
    @bst_byp_en.setter
    def bst_byp_en(self,value):
        self.bst_byp_en_value = value 
        regvalue = self.bst_byp_en
        # perform operation with reg value 
            
    @property
    def bst_zc_en(self):
        self.bst_zc_en_pos   = 6
        self.bst_zc_en_len   = 1
        return self.bst_zc_en_value
        
    @bst_zc_en.setter
    def bst_zc_en(self,value):
        self.bst_zc_en_value = value 
        regvalue = self.bst_zc_en
        # perform operation with reg value 
            
    @property
    def bst_bat_track_en(self):
        self.bst_bat_track_en_pos   = 5
        self.bst_bat_track_en_len   = 1
        return self.bst_bat_track_en_value
        
    @bst_bat_track_en.setter
    def bst_bat_track_en(self,value):
        self.bst_bat_track_en_value = value 
        regvalue = self.bst_bat_track_en
        # perform operation with reg value 
            
    @property
    def bst_mfl_en(self):
        self.bst_mfl_en_pos   = 4
        self.bst_mfl_en_len   = 1
        return self.bst_mfl_en_value
        
    @bst_mfl_en.setter
    def bst_mfl_en(self,value):
        self.bst_mfl_en_value = value 
        regvalue = self.bst_mfl_en
        # perform operation with reg value 
            
    @property
    def bst_env_track_en(self):
        self.bst_env_track_en_pos   = 3
        self.bst_env_track_en_len   = 1
        return self.bst_env_track_en_value
        
    @bst_env_track_en.setter
    def bst_env_track_en(self,value):
        self.bst_env_track_en_value = value 
        regvalue = self.bst_env_track_en
        # perform operation with reg value 
            
    @property
    def bst_ocp_en(self):
        self.bst_ocp_en_pos   = 1
        self.bst_ocp_en_len   = 1
        return self.bst_ocp_en_value
        
    @bst_ocp_en.setter
    def bst_ocp_en(self,value):
        self.bst_ocp_en_value = value 
        regvalue = self.bst_ocp_en
        # perform operation with reg value 
            
    @property
    def bst_en(self):
        self.bst_en_pos   = 0
        self.bst_en_len   = 1
        return self.bst_en_value
        
    @bst_en.setter
    def bst_en(self,value):
        self.bst_en_value = value 
        regvalue = self.bst_en
        # perform operation with reg value 
             
class BST_Comp_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0xb1
        self.page = 0
        
    @property
    def bst_env_err_en(self):
        self.bst_env_err_en_pos   = 7
        self.bst_env_err_en_len   = 1
        return self.bst_env_err_en_value
        
    @bst_env_err_en.setter
    def bst_env_err_en(self,value):
        self.bst_env_err_en_value = value 
        regvalue = self.bst_env_err_en
        # perform operation with reg value 
            
    @property
    def bst_bootstrap_en(self):
        self.bst_bootstrap_en_pos   = 6
        self.bst_bootstrap_en_len   = 1
        return self.bst_bootstrap_en_value
        
    @bst_bootstrap_en.setter
    def bst_bootstrap_en(self,value):
        self.bst_bootstrap_en_value = value 
        regvalue = self.bst_bootstrap_en
        # perform operation with reg value 
            
    @property
    def bst_amp_bias_en(self):
        self.bst_amp_bias_en_pos   = 5
        self.bst_amp_bias_en_len   = 1
        return self.bst_amp_bias_en_value
        
    @bst_amp_bias_en.setter
    def bst_amp_bias_en(self,value):
        self.bst_amp_bias_en_value = value 
        regvalue = self.bst_amp_bias_en
        # perform operation with reg value 
            
    @property
    def bst_amp_bso_en(self):
        self.bst_amp_bso_en_pos   = 4
        self.bst_amp_bso_en_len   = 1
        return self.bst_amp_bso_en_value
        
    @bst_amp_bso_en.setter
    def bst_amp_bso_en(self,value):
        self.bst_amp_bso_en_value = value 
        regvalue = self.bst_amp_bso_en
        # perform operation with reg value 
            
    @property
    def bst_comp_bias_en(self):
        self.bst_comp_bias_en_pos   = 3
        self.bst_comp_bias_en_len   = 1
        return self.bst_comp_bias_en_value
        
    @bst_comp_bias_en.setter
    def bst_comp_bias_en(self,value):
        self.bst_comp_bias_en_value = value 
        regvalue = self.bst_comp_bias_en
        # perform operation with reg value 
            
    @property
    def bst_comp_bso_en(self):
        self.bst_comp_bso_en_pos   = 2
        self.bst_comp_bso_en_len   = 1
        return self.bst_comp_bso_en_value
        
    @bst_comp_bso_en.setter
    def bst_comp_bso_en(self,value):
        self.bst_comp_bso_en_value = value 
        regvalue = self.bst_comp_bso_en
        # perform operation with reg value 
            
    @property
    def bst_bias_ovp_en(self):
        self.bst_bias_ovp_en_pos   = 1
        self.bst_bias_ovp_en_len   = 1
        return self.bst_bias_ovp_en_value
        
    @bst_bias_ovp_en.setter
    def bst_bias_ovp_en(self,value):
        self.bst_bias_ovp_en_value = value 
        regvalue = self.bst_bias_ovp_en
        # perform operation with reg value 
            
    @property
    def bst_bso_ovp_en(self):
        self.bst_bso_ovp_en_pos   = 0
        self.bst_bso_ovp_en_len   = 1
        return self.bst_bso_ovp_en_value
        
    @bst_bso_ovp_en.setter
    def bst_bso_ovp_en(self,value):
        self.bst_bso_ovp_en_value = value 
        regvalue = self.bst_bso_ovp_en
        # perform operation with reg value 
             
class BST_Comp_Register_3 :
    
    def __init__(self) -> None:
        self.address = 0xb2
        self.page = 0
        
    @property
    def bst_mfl_sel1_0(self):
        self.bst_mfl_sel1_0_pos   = 6
        self.bst_mfl_sel1_0_len   = 2
        return self.bst_mfl_sel1_0_value
        
    @bst_mfl_sel1_0.setter
    def bst_mfl_sel1_0(self,value):
        self.bst_mfl_sel1_0_value = value 
        regvalue = self.bst_mfl_sel1_0
        # perform operation with reg value 
            
    @property
    def bst_ovp_bso_sel1_0(self):
        self.bst_ovp_bso_sel1_0_pos   = 4
        self.bst_ovp_bso_sel1_0_len   = 2
        return self.bst_ovp_bso_sel1_0_value
        
    @bst_ovp_bso_sel1_0.setter
    def bst_ovp_bso_sel1_0(self,value):
        self.bst_ovp_bso_sel1_0_value = value 
        regvalue = self.bst_ovp_bso_sel1_0
        # perform operation with reg value 
            
    @property
    def bst_ovp_bias_th1_0(self):
        self.bst_ovp_bias_th1_0_pos   = 2
        self.bst_ovp_bias_th1_0_len   = 2
        return self.bst_ovp_bias_th1_0_value
        
    @bst_ovp_bias_th1_0.setter
    def bst_ovp_bias_th1_0(self,value):
        self.bst_ovp_bias_th1_0_value = value 
        regvalue = self.bst_ovp_bias_th1_0
        # perform operation with reg value 
            
    @property
    def bst_ls_sel(self):
        self.bst_ls_sel_pos   = 1
        self.bst_ls_sel_len   = 1
        return self.bst_ls_sel_value
        
    @bst_ls_sel.setter
    def bst_ls_sel(self,value):
        self.bst_ls_sel_value = value 
        regvalue = self.bst_ls_sel
        # perform operation with reg value 
            
    @property
    def bst_power_force(self):
        self.bst_power_force_pos   = 0
        self.bst_power_force_len   = 1
        return self.bst_power_force_value
        
    @bst_power_force.setter
    def bst_power_force(self,value):
        self.bst_power_force_value = value 
        regvalue = self.bst_power_force
        # perform operation with reg value 
             
class BST_Comp_Register_4 :
    
    def __init__(self) -> None:
        self.address = 0xb3
        self.page = 0
        
    @property
    def bst_lp_en(self):
        self.bst_lp_en_pos   = 5
        self.bst_lp_en_len   = 1
        return self.bst_lp_en_value
        
    @bst_lp_en.setter
    def bst_lp_en(self,value):
        self.bst_lp_en_value = value 
        regvalue = self.bst_lp_en
        # perform operation with reg value 
            
    @property
    def bst_clamp_bias_en(self):
        self.bst_clamp_bias_en_pos   = 4
        self.bst_clamp_bias_en_len   = 1
        return self.bst_clamp_bias_en_value
        
    @bst_clamp_bias_en.setter
    def bst_clamp_bias_en(self,value):
        self.bst_clamp_bias_en_value = value 
        regvalue = self.bst_clamp_bias_en
        # perform operation with reg value 
            
    @property
    def bst_clamp_bso_en(self):
        self.bst_clamp_bso_en_pos   = 3
        self.bst_clamp_bso_en_len   = 1
        return self.bst_clamp_bso_en_value
        
    @bst_clamp_bso_en.setter
    def bst_clamp_bso_en(self,value):
        self.bst_clamp_bso_en_value = value 
        regvalue = self.bst_clamp_bso_en
        # perform operation with reg value 
            
    @property
    def bst_loop_cap_sel2_0(self):
        self.bst_loop_cap_sel2_0_pos   = 0
        self.bst_loop_cap_sel2_0_len   = 3
        return self.bst_loop_cap_sel2_0_value
        
    @bst_loop_cap_sel2_0.setter
    def bst_loop_cap_sel2_0(self,value):
        self.bst_loop_cap_sel2_0_value = value 
        regvalue = self.bst_loop_cap_sel2_0
        # perform operation with reg value 
             
class BST_Comp_Register_5 :
    
    def __init__(self) -> None:
        self.address = 0xb4
        self.page = 0
        
    @property
    def force_bst_env_err(self):
        self.force_bst_env_err_pos   = 3
        self.force_bst_env_err_len   = 1
        return self.force_bst_env_err_value
        
    @force_bst_env_err.setter
    def force_bst_env_err(self,value):
        self.force_bst_env_err_value = value 
        regvalue = self.force_bst_env_err
        # perform operation with reg value 
            
    @property
    def bst_hsb_sel(self):
        self.bst_hsb_sel_pos   = 2
        self.bst_hsb_sel_len   = 1
        return self.bst_hsb_sel_value
        
    @bst_hsb_sel.setter
    def bst_hsb_sel(self,value):
        self.bst_hsb_sel_value = value 
        regvalue = self.bst_hsb_sel
        # perform operation with reg value 
            
    @property
    def bst_hsa_sel(self):
        self.bst_hsa_sel_pos   = 1
        self.bst_hsa_sel_len   = 1
        return self.bst_hsa_sel_value
        
    @bst_hsa_sel.setter
    def bst_hsa_sel(self,value):
        self.bst_hsa_sel_value = value 
        regvalue = self.bst_hsa_sel
        # perform operation with reg value 
            
    @property
    def bst_byp_sel(self):
        self.bst_byp_sel_pos   = 0
        self.bst_byp_sel_len   = 1
        return self.bst_byp_sel_value
        
    @bst_byp_sel.setter
    def bst_byp_sel(self,value):
        self.bst_byp_sel_value = value 
        regvalue = self.bst_byp_sel
        # perform operation with reg value 
             
class BST_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0xc0
        self.page = 0
        
    @property
    def bst_ocp_sel2_0(self):
        self.bst_ocp_sel2_0_pos   = 0
        self.bst_ocp_sel2_0_len   = 3
        return self.bst_ocp_sel2_0_value
        
    @bst_ocp_sel2_0.setter
    def bst_ocp_sel2_0(self,value):
        self.bst_ocp_sel2_0_value = value 
        regvalue = self.bst_ocp_sel2_0
        # perform operation with reg value 
             
class BST_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0xc1
        self.page = 0
        
    @property
    def bst_att_step2_0(self):
        self.bst_att_step2_0_pos   = 4
        self.bst_att_step2_0_len   = 3
        return self.bst_att_step2_0_value
        
    @bst_att_step2_0.setter
    def bst_att_step2_0(self,value):
        self.bst_att_step2_0_value = value 
        regvalue = self.bst_att_step2_0
        # perform operation with reg value 
            
    @property
    def bst_att_time8(self):
        self.bst_att_time8_pos   = 0
        self.bst_att_time8_len   = 1
        return self.bst_att_time8_value
        
    @bst_att_time8.setter
    def bst_att_time8(self,value):
        self.bst_att_time8_value = value 
        regvalue = self.bst_att_time8
        # perform operation with reg value 
             
class BST_Register_3 :
    
    def __init__(self) -> None:
        self.address = 0xc2
        self.page = 0
        
    @property
    def bst_att_time7_0(self):
        self.bst_att_time7_0_pos   = 0
        self.bst_att_time7_0_len   = 8
        return self.bst_att_time7_0_value
        
    @bst_att_time7_0.setter
    def bst_att_time7_0(self,value):
        self.bst_att_time7_0_value = value 
        regvalue = self.bst_att_time7_0
        # perform operation with reg value 
             
class BST_Register_4 :
    
    def __init__(self) -> None:
        self.address = 0xc3
        self.page = 0
        
    @property
    def bst_rel_step2_0(self):
        self.bst_rel_step2_0_pos   = 4
        self.bst_rel_step2_0_len   = 3
        return self.bst_rel_step2_0_value
        
    @bst_rel_step2_0.setter
    def bst_rel_step2_0(self,value):
        self.bst_rel_step2_0_value = value 
        regvalue = self.bst_rel_step2_0
        # perform operation with reg value 
            
    @property
    def bst_rel_time11_8(self):
        self.bst_rel_time11_8_pos   = 0
        self.bst_rel_time11_8_len   = 4
        return self.bst_rel_time11_8_value
        
    @bst_rel_time11_8.setter
    def bst_rel_time11_8(self,value):
        self.bst_rel_time11_8_value = value 
        regvalue = self.bst_rel_time11_8
        # perform operation with reg value 
             
class BST_Register_5 :
    
    def __init__(self) -> None:
        self.address = 0xc4
        self.page = 0
        
    @property
    def bst_rel_time7_0(self):
        self.bst_rel_time7_0_pos   = 0
        self.bst_rel_time7_0_len   = 8
        return self.bst_rel_time7_0_value
        
    @bst_rel_time7_0.setter
    def bst_rel_time7_0(self,value):
        self.bst_rel_time7_0_value = value 
        regvalue = self.bst_rel_time7_0
        # perform operation with reg value 
             
class BST_Register_6 :
    
    def __init__(self) -> None:
        self.address = 0xc5
        self.page = 0
        
    @property
    def bst_rel_time_pd_sel(self):
        self.bst_rel_time_pd_sel_pos   = 4
        self.bst_rel_time_pd_sel_len   = 1
        return self.bst_rel_time_pd_sel_value
        
    @bst_rel_time_pd_sel.setter
    def bst_rel_time_pd_sel(self,value):
        self.bst_rel_time_pd_sel_value = value 
        regvalue = self.bst_rel_time_pd_sel
        # perform operation with reg value 
            
    @property
    def bst_rel_time_fault11_8(self):
        self.bst_rel_time_fault11_8_pos   = 0
        self.bst_rel_time_fault11_8_len   = 4
        return self.bst_rel_time_fault11_8_value
        
    @bst_rel_time_fault11_8.setter
    def bst_rel_time_fault11_8(self,value):
        self.bst_rel_time_fault11_8_value = value 
        regvalue = self.bst_rel_time_fault11_8
        # perform operation with reg value 
             
class BST_Register_7 :
    
    def __init__(self) -> None:
        self.address = 0xc6
        self.page = 0
        
    @property
    def bst_rel_time_fault7_0(self):
        self.bst_rel_time_fault7_0_pos   = 0
        self.bst_rel_time_fault7_0_len   = 8
        return self.bst_rel_time_fault7_0_value
        
    @bst_rel_time_fault7_0.setter
    def bst_rel_time_fault7_0(self,value):
        self.bst_rel_time_fault7_0_value = value 
        regvalue = self.bst_rel_time_fault7_0
        # perform operation with reg value 
             
class BST_Register_8 :
    
    def __init__(self) -> None:
        self.address = 0xc7
        self.page = 0
        
    @property
    def bst_first_step2_0(self):
        self.bst_first_step2_0_pos   = 4
        self.bst_first_step2_0_len   = 3
        return self.bst_first_step2_0_value
        
    @bst_first_step2_0.setter
    def bst_first_step2_0(self,value):
        self.bst_first_step2_0_value = value 
        regvalue = self.bst_first_step2_0
        # perform operation with reg value 
            
    @property
    def bst_byp_track_time3_0(self):
        self.bst_byp_track_time3_0_pos   = 0
        self.bst_byp_track_time3_0_len   = 4
        return self.bst_byp_track_time3_0_value
        
    @bst_byp_track_time3_0.setter
    def bst_byp_track_time3_0(self,value):
        self.bst_byp_track_time3_0_value = value 
        regvalue = self.bst_byp_track_time3_0
        # perform operation with reg value 
             
class BST_Register_9 :
    
    def __init__(self) -> None:
        self.address = 0xc8
        self.page = 0
        
    @property
    def bst_dgltch_byp2_0(self):
        self.bst_dgltch_byp2_0_pos   = 0
        self.bst_dgltch_byp2_0_len   = 3
        return self.bst_dgltch_byp2_0_value
        
    @bst_dgltch_byp2_0.setter
    def bst_dgltch_byp2_0(self,value):
        self.bst_dgltch_byp2_0_value = value 
        regvalue = self.bst_dgltch_byp2_0
        # perform operation with reg value 
             
class BST_Register_10 :
    
    def __init__(self) -> None:
        self.address = 0xc9
        self.page = 0
        
    @property
    def bst_dc_bias4_0(self):
        self.bst_dc_bias4_0_pos   = 0
        self.bst_dc_bias4_0_len   = 5
        return self.bst_dc_bias4_0_value
        
    @bst_dc_bias4_0.setter
    def bst_dc_bias4_0(self,value):
        self.bst_dc_bias4_0_value = value 
        regvalue = self.bst_dc_bias4_0
        # perform operation with reg value 
             
class BST_Register_11 :
    
    def __init__(self) -> None:
        self.address = 0xca
        self.page = 0
        
    @property
    def bst_bso6_0(self):
        self.bst_bso6_0_pos   = 0
        self.bst_bso6_0_len   = 7
        return self.bst_bso6_0_value
        
    @bst_bso6_0.setter
    def bst_bso6_0(self,value):
        self.bst_bso6_0_value = value 
        regvalue = self.bst_bso6_0
        # perform operation with reg value 
             
class BST_Register_12 :
    
    def __init__(self) -> None:
        self.address = 0xcb
        self.page = 0
        
    @property
    def bst_bso_head_range_dis(self):
        self.bst_bso_head_range_dis_pos   = 7
        self.bst_bso_head_range_dis_len   = 1
        return self.bst_bso_head_range_dis_value
        
    @bst_bso_head_range_dis.setter
    def bst_bso_head_range_dis(self,value):
        self.bst_bso_head_range_dis_value = value 
        regvalue = self.bst_bso_head_range_dis
        # perform operation with reg value 
            
    @property
    def bst_bso_head_range_sel6_0(self):
        self.bst_bso_head_range_sel6_0_pos   = 0
        self.bst_bso_head_range_sel6_0_len   = 7
        return self.bst_bso_head_range_sel6_0_value
        
    @bst_bso_head_range_sel6_0.setter
    def bst_bso_head_range_sel6_0(self,value):
        self.bst_bso_head_range_sel6_0_value = value 
        regvalue = self.bst_bso_head_range_sel6_0
        # perform operation with reg value 
             
class BST_Register_13 :
    
    def __init__(self) -> None:
        self.address = 0xcc
        self.page = 0
        
    @property
    def bst_bso_head_low_range4_0(self):
        self.bst_bso_head_low_range4_0_pos   = 0
        self.bst_bso_head_low_range4_0_len   = 5
        return self.bst_bso_head_low_range4_0_value
        
    @bst_bso_head_low_range4_0.setter
    def bst_bso_head_low_range4_0(self,value):
        self.bst_bso_head_low_range4_0_value = value 
        regvalue = self.bst_bso_head_low_range4_0
        # perform operation with reg value 
             
class BST_Register_14 :
    
    def __init__(self) -> None:
        self.address = 0xcd
        self.page = 0
        
    @property
    def bst_bso_head_high_range4_0(self):
        self.bst_bso_head_high_range4_0_pos   = 0
        self.bst_bso_head_high_range4_0_len   = 5
        return self.bst_bso_head_high_range4_0_value
        
    @bst_bso_head_high_range4_0.setter
    def bst_bso_head_high_range4_0(self,value):
        self.bst_bso_head_high_range4_0_value = value 
        regvalue = self.bst_bso_head_high_range4_0
        # perform operation with reg value 
             
class BST_Register_15 :
    
    def __init__(self) -> None:
        self.address = 0xce
        self.page = 0
        
    @property
    def bst_head_track_high_range2_0(self):
        self.bst_head_track_high_range2_0_pos   = 4
        self.bst_head_track_high_range2_0_len   = 3
        return self.bst_head_track_high_range2_0_value
        
    @bst_head_track_high_range2_0.setter
    def bst_head_track_high_range2_0(self,value):
        self.bst_head_track_high_range2_0_value = value 
        regvalue = self.bst_head_track_high_range2_0
        # perform operation with reg value 
            
    @property
    def bst_head_track_low_range2_0(self):
        self.bst_head_track_low_range2_0_pos   = 0
        self.bst_head_track_low_range2_0_len   = 3
        return self.bst_head_track_low_range2_0_value
        
    @bst_head_track_low_range2_0.setter
    def bst_head_track_low_range2_0(self,value):
        self.bst_head_track_low_range2_0_value = value 
        regvalue = self.bst_head_track_low_range2_0
        # perform operation with reg value 
             
class BST_Register_16 :
    
    def __init__(self) -> None:
        self.address = 0xcf
        self.page = 0
        
    @property
    def et_state3_0(self):
        self.et_state3_0_pos   = 0
        self.et_state3_0_len   = 4
        return self.et_state3_0_value
        
    @et_state3_0.setter
    def et_state3_0(self,value):
        self.et_state3_0_value = value 
        regvalue = self.et_state3_0
        # perform operation with reg value 
             
class ET_Spare_Register :
    
    def __init__(self) -> None:
        self.address = 0xdf
        self.page = 0
        
    @property
    def et_spare7_0(self):
        self.et_spare7_0_pos   = 0
        self.et_spare7_0_len   = 8
        return self.et_spare7_0_value
        
    @et_spare7_0.setter
    def et_spare7_0(self,value):
        self.et_spare7_0_value = value 
        regvalue = self.et_spare7_0
        # perform operation with reg value 
             
class CAL_Register_1 :
    
    def __init__(self) -> None:
        self.address = 0xe0
        self.page = 0
        
    @property
    def dpa_inana_calib_dis(self):
        self.dpa_inana_calib_dis_pos   = 4
        self.dpa_inana_calib_dis_len   = 1
        return self.dpa_inana_calib_dis_value
        
    @dpa_inana_calib_dis.setter
    def dpa_inana_calib_dis(self,value):
        self.dpa_inana_calib_dis_value = value 
        regvalue = self.dpa_inana_calib_dis
        # perform operation with reg value 
            
    @property
    def azmode_time1_0(self):
        self.azmode_time1_0_pos   = 2
        self.azmode_time1_0_len   = 2
        return self.azmode_time1_0_value
        
    @azmode_time1_0.setter
    def azmode_time1_0(self,value):
        self.azmode_time1_0_value = value 
        regvalue = self.azmode_time1_0
        # perform operation with reg value 
            
    @property
    def cal_measure_time1_0(self):
        self.cal_measure_time1_0_pos   = 0
        self.cal_measure_time1_0_len   = 2
        return self.cal_measure_time1_0_value
        
    @cal_measure_time1_0.setter
    def cal_measure_time1_0(self,value):
        self.cal_measure_time1_0_value = value 
        regvalue = self.cal_measure_time1_0
        # perform operation with reg value 
             
class CAL_Register_2 :
    
    def __init__(self) -> None:
        self.address = 0xe1
        self.page = 0
        
    @property
    def offs_comp_en(self):
        self.offs_comp_en_pos   = 4
        self.offs_comp_en_len   = 1
        return self.offs_comp_en_value
        
    @offs_comp_en.setter
    def offs_comp_en(self,value):
        self.offs_comp_en_value = value 
        regvalue = self.offs_comp_en
        # perform operation with reg value 
            
    @property
    def azcomp_isel1c1_0(self):
        self.azcomp_isel1c1_0_pos   = 2
        self.azcomp_isel1c1_0_len   = 2
        return self.azcomp_isel1c1_0_value
        
    @azcomp_isel1c1_0.setter
    def azcomp_isel1c1_0(self,value):
        self.azcomp_isel1c1_0_value = value 
        regvalue = self.azcomp_isel1c1_0
        # perform operation with reg value 
            
    @property
    def azcomp_isel2c1_0(self):
        self.azcomp_isel2c1_0_pos   = 0
        self.azcomp_isel2c1_0_len   = 2
        return self.azcomp_isel2c1_0_value
        
    @azcomp_isel2c1_0.setter
    def azcomp_isel2c1_0(self,value):
        self.azcomp_isel2c1_0_value = value 
        regvalue = self.azcomp_isel2c1_0
        # perform operation with reg value 
             
class CAL_Register_3 :
    
    def __init__(self) -> None:
        self.address = 0xe2
        self.page = 0
        
    @property
    def ext_cal_offs(self):
        self.ext_cal_offs_pos   = 1
        self.ext_cal_offs_len   = 1
        return self.ext_cal_offs_value
        
    @ext_cal_offs.setter
    def ext_cal_offs(self,value):
        self.ext_cal_offs_value = value 
        regvalue = self.ext_cal_offs
        # perform operation with reg value 
            
    @property
    def int_cal_offs(self):
        self.int_cal_offs_pos   = 0
        self.int_cal_offs_len   = 1
        return self.int_cal_offs_value
        
    @int_cal_offs.setter
    def int_cal_offs(self,value):
        self.int_cal_offs_value = value 
        regvalue = self.int_cal_offs
        # perform operation with reg value 
             
class CAL_Register_4 :
    
    def __init__(self) -> None:
        self.address = 0xe3
        self.page = 0
        
    @property
    def ana_idle_ext_cal_polarity(self):
        self.ana_idle_ext_cal_polarity_pos   = 7
        self.ana_idle_ext_cal_polarity_len   = 1
        return self.ana_idle_ext_cal_polarity_value
        
    @ana_idle_ext_cal_polarity.setter
    def ana_idle_ext_cal_polarity(self,value):
        self.ana_idle_ext_cal_polarity_value = value 
        regvalue = self.ana_idle_ext_cal_polarity
        # perform operation with reg value 
            
    @property
    def ana_idle_int_cal_polarity(self):
        self.ana_idle_int_cal_polarity_pos   = 6
        self.ana_idle_int_cal_polarity_len   = 1
        return self.ana_idle_int_cal_polarity_value
        
    @ana_idle_int_cal_polarity.setter
    def ana_idle_int_cal_polarity(self,value):
        self.ana_idle_int_cal_polarity_value = value 
        regvalue = self.ana_idle_int_cal_polarity
        # perform operation with reg value 
            
    @property
    def ana_zero_ext_cal_polarity(self):
        self.ana_zero_ext_cal_polarity_pos   = 5
        self.ana_zero_ext_cal_polarity_len   = 1
        return self.ana_zero_ext_cal_polarity_value
        
    @ana_zero_ext_cal_polarity.setter
    def ana_zero_ext_cal_polarity(self,value):
        self.ana_zero_ext_cal_polarity_value = value 
        regvalue = self.ana_zero_ext_cal_polarity
        # perform operation with reg value 
            
    @property
    def ana_zero_int_cal_polarity(self):
        self.ana_zero_int_cal_polarity_pos   = 4
        self.ana_zero_int_cal_polarity_len   = 1
        return self.ana_zero_int_cal_polarity_value
        
    @ana_zero_int_cal_polarity.setter
    def ana_zero_int_cal_polarity(self,value):
        self.ana_zero_int_cal_polarity_value = value 
        regvalue = self.ana_zero_int_cal_polarity
        # perform operation with reg value 
            
    @property
    def dig_idle_ext_cal_polarity(self):
        self.dig_idle_ext_cal_polarity_pos   = 3
        self.dig_idle_ext_cal_polarity_len   = 1
        return self.dig_idle_ext_cal_polarity_value
        
    @dig_idle_ext_cal_polarity.setter
    def dig_idle_ext_cal_polarity(self,value):
        self.dig_idle_ext_cal_polarity_value = value 
        regvalue = self.dig_idle_ext_cal_polarity
        # perform operation with reg value 
            
    @property
    def dig_idle_int_cal_polarity(self):
        self.dig_idle_int_cal_polarity_pos   = 2
        self.dig_idle_int_cal_polarity_len   = 1
        return self.dig_idle_int_cal_polarity_value
        
    @dig_idle_int_cal_polarity.setter
    def dig_idle_int_cal_polarity(self,value):
        self.dig_idle_int_cal_polarity_value = value 
        regvalue = self.dig_idle_int_cal_polarity
        # perform operation with reg value 
            
    @property
    def dig_zero_ext_cal_polarity(self):
        self.dig_zero_ext_cal_polarity_pos   = 1
        self.dig_zero_ext_cal_polarity_len   = 1
        return self.dig_zero_ext_cal_polarity_value
        
    @dig_zero_ext_cal_polarity.setter
    def dig_zero_ext_cal_polarity(self,value):
        self.dig_zero_ext_cal_polarity_value = value 
        regvalue = self.dig_zero_ext_cal_polarity
        # perform operation with reg value 
            
    @property
    def dig_zero_int_cal_polarity(self):
        self.dig_zero_int_cal_polarity_pos   = 0
        self.dig_zero_int_cal_polarity_len   = 1
        return self.dig_zero_int_cal_polarity_value
        
    @dig_zero_int_cal_polarity.setter
    def dig_zero_int_cal_polarity(self,value):
        self.dig_zero_int_cal_polarity_value = value 
        regvalue = self.dig_zero_int_cal_polarity
        # perform operation with reg value 
             
class CAL_Register_5 :
    
    def __init__(self) -> None:
        self.address = 0xe4
        self.page = 0
        
    @property
    def azcomp_trig(self):
        self.azcomp_trig_pos   = 0
        self.azcomp_trig_len   = 1
        return self.azcomp_trig_value
        
    @azcomp_trig.setter
    def azcomp_trig(self,value):
        self.azcomp_trig_value = value 
        regvalue = self.azcomp_trig
        # perform operation with reg value 
             
class CAL_Register_6 :
    
    def __init__(self) -> None:
        self.address = 0xe5
        self.page = 0
        
    @property
    def cal_offs_end(self):
        self.cal_offs_end_pos   = 4
        self.cal_offs_end_len   = 1
        return self.cal_offs_end_value
        
    @cal_offs_end.setter
    def cal_offs_end(self,value):
        self.cal_offs_end_value = value 
        regvalue = self.cal_offs_end
        # perform operation with reg value 
            
    @property
    def azcomp_sat_zero(self):
        self.azcomp_sat_zero_pos   = 3
        self.azcomp_sat_zero_len   = 1
        return self.azcomp_sat_zero_value
        
    @azcomp_sat_zero.setter
    def azcomp_sat_zero(self,value):
        self.azcomp_sat_zero_value = value 
        regvalue = self.azcomp_sat_zero
        # perform operation with reg value 
            
    @property
    def azcomp_sat_idle(self):
        self.azcomp_sat_idle_pos   = 2
        self.azcomp_sat_idle_len   = 1
        return self.azcomp_sat_idle_value
        
    @azcomp_sat_idle.setter
    def azcomp_sat_idle(self,value):
        self.azcomp_sat_idle_value = value 
        regvalue = self.azcomp_sat_idle
        # perform operation with reg value 
            
    @property
    def azcomp_out(self):
        self.azcomp_out_pos   = 1
        self.azcomp_out_len   = 1
        return self.azcomp_out_value
        
    @azcomp_out.setter
    def azcomp_out(self,value):
        self.azcomp_out_value = value 
        regvalue = self.azcomp_out
        # perform operation with reg value 
            
    @property
    def azcomp_ready(self):
        self.azcomp_ready_pos   = 0
        self.azcomp_ready_len   = 1
        return self.azcomp_ready_value
        
    @azcomp_ready.setter
    def azcomp_ready(self,value):
        self.azcomp_ready_value = value 
        regvalue = self.azcomp_ready
        # perform operation with reg value 
             
class CAL_Spare_Register :
    
    def __init__(self) -> None:
        self.address = 0xef
        self.page = 0
        
    @property
    def cal_spare7_0(self):
        self.cal_spare7_0_pos   = 0
        self.cal_spare7_0_len   = 8
        return self.cal_spare7_0_value
        
    @cal_spare7_0.setter
    def cal_spare7_0(self,value):
        self.cal_spare7_0_value = value 
        regvalue = self.cal_spare7_0
        # perform operation with reg value 
             
class PAD_settings :
    
    def __init__(self) -> None:
        self.address = 0xfc
        self.page = 0
        
    @property
    def tdm_pad_di_en(self):
        self.tdm_pad_di_en_pos   = 2
        self.tdm_pad_di_en_len   = 1
        return self.tdm_pad_di_en_value
        
    @tdm_pad_di_en.setter
    def tdm_pad_di_en(self,value):
        self.tdm_pad_di_en_value = value 
        regvalue = self.tdm_pad_di_en
        # perform operation with reg value 
             
class Page_selection :
    
    def __init__(self) -> None:
        self.address = 0xfe
        self.page = 1
        
    @property
    def i2c_page_sel1_0(self):
        self.i2c_page_sel1_0_pos   = 0
        self.i2c_page_sel1_0_len   = 2
        return self.i2c_page_sel1_0_value
        
    @i2c_page_sel1_0.setter
    def i2c_page_sel1_0(self,value):
        self.i2c_page_sel1_0_value = value 
        regvalue = self.i2c_page_sel1_0
        # perform operation with reg value 
            
    @property
    def i2c_page_sel1_0(self):
        self.i2c_page_sel1_0_pos   = 0
        self.i2c_page_sel1_0_len   = 2
        return self.i2c_page_sel1_0_value
        
    @i2c_page_sel1_0.setter
    def i2c_page_sel1_0(self,value):
        self.i2c_page_sel1_0_value = value 
        regvalue = self.i2c_page_sel1_0
        # perform operation with reg value 
             
class Device_Info :
    
    def __init__(self) -> None:
        self.address = 0xff
        self.page = 1
        
    @property
    def device_id4_0(self):
        self.device_id4_0_pos   = 3
        self.device_id4_0_len   = 5
        return self.device_id4_0_value
        
    @device_id4_0.setter
    def device_id4_0(self,value):
        self.device_id4_0_value = value 
        regvalue = self.device_id4_0
        # perform operation with reg value 
            
    @property
    def version_id2_0(self):
        self.version_id2_0_pos   = 0
        self.version_id2_0_len   = 3
        return self.version_id2_0_value
        
    @version_id2_0.setter
    def version_id2_0(self,value):
        self.version_id2_0_value = value 
        regvalue = self.version_id2_0
        # perform operation with reg value 
            
    @property
    def device_id4_0(self):
        self.device_id4_0_pos   = 3
        self.device_id4_0_len   = 5
        return self.device_id4_0_value
        
    @device_id4_0.setter
    def device_id4_0(self,value):
        self.device_id4_0_value = value 
        regvalue = self.device_id4_0
        # perform operation with reg value 
            
    @property
    def version_id2_0(self):
        self.version_id2_0_pos   = 0
        self.version_id2_0_len   = 3
        return self.version_id2_0_value
        
    @version_id2_0.setter
    def version_id2_0(self,value):
        self.version_id2_0_value = value 
        regvalue = self.version_id2_0
        # perform operation with reg value 
             
class IO_Test_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x0
        self.page = 1
        
    @property
    def io_tst_en(self):
        self.io_tst_en_pos   = 3
        self.io_tst_en_len   = 1
        return self.io_tst_en_value
        
    @io_tst_en.setter
    def io_tst_en(self,value):
        self.io_tst_en_value = value 
        regvalue = self.io_tst_en
        # perform operation with reg value 
            
    @property
    def io_tst_mode2_0(self):
        self.io_tst_mode2_0_pos   = 0
        self.io_tst_mode2_0_len   = 3
        return self.io_tst_mode2_0_value
        
    @io_tst_mode2_0.setter
    def io_tst_mode2_0(self,value):
        self.io_tst_mode2_0_value = value 
        regvalue = self.io_tst_mode2_0
        # perform operation with reg value 
             
class IO_Test_settings_2 :
    
    def __init__(self) -> None:
        self.address = 0x1
        self.page = 1
        
    @property
    def io_tst_wr2_0(self):
        self.io_tst_wr2_0_pos   = 0
        self.io_tst_wr2_0_len   = 3
        return self.io_tst_wr2_0_value
        
    @io_tst_wr2_0.setter
    def io_tst_wr2_0(self,value):
        self.io_tst_wr2_0_value = value 
        regvalue = self.io_tst_wr2_0
        # perform operation with reg value 
             
class IO_Test_settings_3 :
    
    def __init__(self) -> None:
        self.address = 0x2
        self.page = 1
        
    @property
    def io_tst_rd4_0(self):
        self.io_tst_rd4_0_pos   = 0
        self.io_tst_rd4_0_len   = 5
        return self.io_tst_rd4_0_value
        
    @io_tst_rd4_0.setter
    def io_tst_rd4_0(self,value):
        self.io_tst_rd4_0_value = value 
        regvalue = self.io_tst_rd4_0
        # perform operation with reg value 
             
class Digital_Test_settings_1 :
    
    def __init__(self) -> None:
        self.address = 0x3
        self.page = 1
        
    @property
    def dig_test_en4_0(self):
        self.dig_test_en4_0_pos   = 0
        self.dig_test_en4_0_len   = 5
        return self.dig_test_en4_0_value
        
    @dig_test_en4_0.setter
    def dig_test_en4_0(self,value):
        self.dig_test_en4_0_value = value 
        regvalue = self.dig_test_en4_0
        # perform operation with reg value 
             
class Digital_Test_settings_2 :
    
    def __init__(self) -> None:
        self.address = 0x4
        self.page = 1
        
    @property
    def dig_test_sel7_0(self):
        self.dig_test_sel7_0_pos   = 0
        self.dig_test_sel7_0_len   = 8
        return self.dig_test_sel7_0_value
        
    @dig_test_sel7_0.setter
    def dig_test_sel7_0(self,value):
        self.dig_test_sel7_0_value = value 
        regvalue = self.dig_test_sel7_0
        # perform operation with reg value 
             
class SCAN_Test :
    
    def __init__(self) -> None:
        self.address = 0x5
        self.page = 1
        
    @property
    def scan_exit_dis(self):
        self.scan_exit_dis_pos   = 6
        self.scan_exit_dis_len   = 1
        return self.scan_exit_dis_value
        
    @scan_exit_dis.setter
    def scan_exit_dis(self,value):
        self.scan_exit_dis_value = value 
        regvalue = self.scan_exit_dis
        # perform operation with reg value 
            
    @property
    def resume_from_scan(self):
        self.resume_from_scan_pos   = 5
        self.resume_from_scan_len   = 1
        return self.resume_from_scan_value
        
    @resume_from_scan.setter
    def resume_from_scan(self,value):
        self.resume_from_scan_value = value 
        regvalue = self.resume_from_scan
        # perform operation with reg value 
            
    @property
    def tdm_pad_dsr(self):
        self.tdm_pad_dsr_pos   = 4
        self.tdm_pad_dsr_len   = 1
        return self.tdm_pad_dsr_value
        
    @tdm_pad_dsr.setter
    def tdm_pad_dsr(self,value):
        self.tdm_pad_dsr_value = value 
        regvalue = self.tdm_pad_dsr
        # perform operation with reg value 
            
    @property
    def dig_pad_dsr(self):
        self.dig_pad_dsr_pos   = 3
        self.dig_pad_dsr_len   = 1
        return self.dig_pad_dsr_value
        
    @dig_pad_dsr.setter
    def dig_pad_dsr(self,value):
        self.dig_pad_dsr_value = value 
        regvalue = self.dig_pad_dsr
        # perform operation with reg value 
            
    @property
    def scan_enh(self):
        self.scan_enh_pos   = 1
        self.scan_enh_len   = 1
        return self.scan_enh_value
        
    @scan_enh.setter
    def scan_enh(self,value):
        self.scan_enh_value = value 
        regvalue = self.scan_enh
        # perform operation with reg value 
            
    @property
    def scanx_enh(self):
        self.scanx_enh_pos   = 0
        self.scanx_enh_len   = 1
        return self.scanx_enh_value
        
    @scanx_enh.setter
    def scanx_enh(self,value):
        self.scanx_enh_value = value 
        regvalue = self.scanx_enh
        # perform operation with reg value 
             
class BIST_reg :
    
    def __init__(self) -> None:
        self.address = 0x6
        self.page = 1
        
    @property
    def bist_end(self):
        self.bist_end_pos   = 5
        self.bist_end_len   = 1
        return self.bist_end_value
        
    @bist_end.setter
    def bist_end(self,value):
        self.bist_end_value = value 
        regvalue = self.bist_end
        # perform operation with reg value 
            
    @property
    def bist_result(self):
        self.bist_result_pos   = 4
        self.bist_result_len   = 1
        return self.bist_result_value
        
    @bist_result.setter
    def bist_result(self,value):
        self.bist_result_value = value 
        regvalue = self.bist_result
        # perform operation with reg value 
            
    @property
    def bist_polarity(self):
        self.bist_polarity_pos   = 1
        self.bist_polarity_len   = 1
        return self.bist_polarity_value
        
    @bist_polarity.setter
    def bist_polarity(self,value):
        self.bist_polarity_value = value 
        regvalue = self.bist_polarity
        # perform operation with reg value 
            
    @property
    def bist_en(self):
        self.bist_en_pos   = 0
        self.bist_en_len   = 1
        return self.bist_en_value
        
    @bist_en.setter
    def bist_en(self,value):
        self.bist_en_value = value 
        regvalue = self.bist_en
        # perform operation with reg value 
             
class Digital_Test_settings_3 :
    
    def __init__(self) -> None:
        self.address = 0x7
        self.page = 1
        
    @property
    def tmux_cnt_sel1_0(self):
        self.tmux_cnt_sel1_0_pos   = 0
        self.tmux_cnt_sel1_0_len   = 2
        return self.tmux_cnt_sel1_0_value
        
    @tmux_cnt_sel1_0.setter
    def tmux_cnt_sel1_0(self,value):
        self.tmux_cnt_sel1_0_value = value 
        regvalue = self.tmux_cnt_sel1_0
        # perform operation with reg value 
             
class DAC_test_1 :
    
    def __init__(self) -> None:
        self.address = 0x8
        self.page = 1
        
    @property
    def tst_dac(self):
        self.tst_dac_pos   = 7
        self.tst_dac_len   = 1
        return self.tst_dac_value
        
    @tst_dac.setter
    def tst_dac(self,value):
        self.tst_dac_value = value 
        regvalue = self.tst_dac
        # perform operation with reg value 
            
    @property
    def tst_data_dwa6_0(self):
        self.tst_data_dwa6_0_pos   = 0
        self.tst_data_dwa6_0_len   = 7
        return self.tst_data_dwa6_0_value
        
    @tst_data_dwa6_0.setter
    def tst_data_dwa6_0(self,value):
        self.tst_data_dwa6_0_value = value 
        regvalue = self.tst_data_dwa6_0
        # perform operation with reg value 
             
class DAC_test_2 :
    
    def __init__(self) -> None:
        self.address = 0x9
        self.page = 1
        
    @property
    def tst_idx_pos_dwa5_0(self):
        self.tst_idx_pos_dwa5_0_pos   = 0
        self.tst_idx_pos_dwa5_0_len   = 6
        return self.tst_idx_pos_dwa5_0_value
        
    @tst_idx_pos_dwa5_0.setter
    def tst_idx_pos_dwa5_0(self,value):
        self.tst_idx_pos_dwa5_0_value = value 
        regvalue = self.tst_idx_pos_dwa5_0
        # perform operation with reg value 
             
class DAC_test_3 :
    
    def __init__(self) -> None:
        self.address = 0xa
        self.page = 1
        
    @property
    def tst_idx_neg_dwa5_0(self):
        self.tst_idx_neg_dwa5_0_pos   = 0
        self.tst_idx_neg_dwa5_0_len   = 6
        return self.tst_idx_neg_dwa5_0_value
        
    @tst_idx_neg_dwa5_0.setter
    def tst_idx_neg_dwa5_0(self,value):
        self.tst_idx_neg_dwa5_0_value = value 
        regvalue = self.tst_idx_neg_dwa5_0
        # perform operation with reg value 
             
class SEQ_settings :
    
    def __init__(self) -> None:
        self.address = 0xc
        self.page = 1
        
    @property
    def seq_prog_latch_dis(self):
        self.seq_prog_latch_dis_pos   = 0
        self.seq_prog_latch_dis_len   = 1
        return self.seq_prog_latch_dis_value
        
    @seq_prog_latch_dis.setter
    def seq_prog_latch_dis(self,value):
        self.seq_prog_latch_dis_value = value 
        regvalue = self.seq_prog_latch_dis
        # perform operation with reg value 
             
class DAC_clock_setting :
    
    def __init__(self) -> None:
        self.address = 0xd
        self.page = 1
        
    @property
    def cal_dac_clk_polarity(self):
        self.cal_dac_clk_polarity_pos   = 3
        self.cal_dac_clk_polarity_len   = 1
        return self.cal_dac_clk_polarity_value
        
    @cal_dac_clk_polarity.setter
    def cal_dac_clk_polarity(self,value):
        self.cal_dac_clk_polarity_value = value 
        regvalue = self.cal_dac_clk_polarity
        # perform operation with reg value 
            
    @property
    def pdm_dac_clk_polarity(self):
        self.pdm_dac_clk_polarity_pos   = 2
        self.pdm_dac_clk_polarity_len   = 1
        return self.pdm_dac_clk_polarity_value
        
    @pdm_dac_clk_polarity.setter
    def pdm_dac_clk_polarity(self,value):
        self.pdm_dac_clk_polarity_value = value 
        regvalue = self.pdm_dac_clk_polarity
        # perform operation with reg value 
            
    @property
    def tdm_dac_clk_delay1_0(self):
        self.tdm_dac_clk_delay1_0_pos   = 0
        self.tdm_dac_clk_delay1_0_len   = 2
        return self.tdm_dac_clk_delay1_0_value
        
    @tdm_dac_clk_delay1_0.setter
    def tdm_dac_clk_delay1_0(self,value):
        self.tdm_dac_clk_delay1_0_value = value 
        regvalue = self.tdm_dac_clk_delay1_0
        # perform operation with reg value 
             
class FRO_clock_mux_setting :
    
    def __init__(self) -> None:
        self.address = 0xe
        self.page = 1
        
    @property
    def pdm_fro_mux_en(self):
        self.pdm_fro_mux_en_pos   = 1
        self.pdm_fro_mux_en_len   = 1
        return self.pdm_fro_mux_en_value
        
    @pdm_fro_mux_en.setter
    def pdm_fro_mux_en(self,value):
        self.pdm_fro_mux_en_value = value 
        regvalue = self.pdm_fro_mux_en
        # perform operation with reg value 
            
    @property
    def tdm_fro_mux_en(self):
        self.tdm_fro_mux_en_pos   = 0
        self.tdm_fro_mux_en_len   = 1
        return self.tdm_fro_mux_en_value
        
    @tdm_fro_mux_en.setter
    def tdm_fro_mux_en(self,value):
        self.tdm_fro_mux_en_value = value 
        regvalue = self.tdm_fro_mux_en
        # perform operation with reg value 
             
class Analog_register_0__Force :
    
    def __init__(self) -> None:
        self.address = 0xf
        self.page = 1
        
    @property
    def force_otp_clock_on(self):
        self.force_otp_clock_on_pos   = 7
        self.force_otp_clock_on_len   = 1
        return self.force_otp_clock_on_value
        
    @force_otp_clock_on.setter
    def force_otp_clock_on(self,value):
        self.force_otp_clock_on_value = value 
        regvalue = self.force_otp_clock_on
        # perform operation with reg value 
            
    @property
    def force_mod_clock_on(self):
        self.force_mod_clock_on_pos   = 6
        self.force_mod_clock_on_len   = 1
        return self.force_mod_clock_on_value
        
    @force_mod_clock_on.setter
    def force_mod_clock_on(self,value):
        self.force_mod_clock_on_value = value 
        regvalue = self.force_mod_clock_on
        # perform operation with reg value 
            
    @property
    def force_bst_bias(self):
        self.force_bst_bias_pos   = 5
        self.force_bst_bias_len   = 1
        return self.force_bst_bias_value
        
    @force_bst_bias.setter
    def force_bst_bias(self,value):
        self.force_bst_bias_value = value 
        regvalue = self.force_bst_bias
        # perform operation with reg value 
            
    @property
    def force_bst_bso(self):
        self.force_bst_bso_pos   = 4
        self.force_bst_bso_len   = 1
        return self.force_bst_bso_value
        
    @force_bst_bso.setter
    def force_bst_bso(self,value):
        self.force_bst_bso_value = value 
        regvalue = self.force_bst_bso
        # perform operation with reg value 
            
    @property
    def force_ref_sdwn_b_dis(self):
        self.force_ref_sdwn_b_dis_pos   = 3
        self.force_ref_sdwn_b_dis_len   = 1
        return self.force_ref_sdwn_b_dis_value
        
    @force_ref_sdwn_b_dis.setter
    def force_ref_sdwn_b_dis(self,value):
        self.force_ref_sdwn_b_dis_value = value 
        regvalue = self.force_ref_sdwn_b_dis
        # perform operation with reg value 
            
    @property
    def force_intfb_en(self):
        self.force_intfb_en_pos   = 2
        self.force_intfb_en_len   = 1
        return self.force_intfb_en_value
        
    @force_intfb_en.setter
    def force_intfb_en(self,value):
        self.force_intfb_en_value = value 
        regvalue = self.force_intfb_en
        # perform operation with reg value 
            
    @property
    def force_pa_pd_d(self):
        self.force_pa_pd_d_pos   = 1
        self.force_pa_pd_d_len   = 1
        return self.force_pa_pd_d_value
        
    @force_pa_pd_d.setter
    def force_pa_pd_d(self,value):
        self.force_pa_pd_d_value = value 
        regvalue = self.force_pa_pd_d
        # perform operation with reg value 
            
    @property
    def force_pa_pd(self):
        self.force_pa_pd_pos   = 0
        self.force_pa_pd_len   = 1
        return self.force_pa_pd_value
        
    @force_pa_pd.setter
    def force_pa_pd(self,value):
        self.force_pa_pd_value = value 
        regvalue = self.force_pa_pd
        # perform operation with reg value 
             
class Analog_register_1__Force :
    
    def __init__(self) -> None:
        self.address = 0x10
        self.page = 1
        
    @property
    def force_dac3_frz(self):
        self.force_dac3_frz_pos   = 7
        self.force_dac3_frz_len   = 1
        return self.force_dac3_frz_value
        
    @force_dac3_frz.setter
    def force_dac3_frz(self,value):
        self.force_dac3_frz_value = value 
        regvalue = self.force_dac3_frz
        # perform operation with reg value 
            
    @property
    def force_dac2_frz(self):
        self.force_dac2_frz_pos   = 6
        self.force_dac2_frz_len   = 1
        return self.force_dac2_frz_value
        
    @force_dac2_frz.setter
    def force_dac2_frz(self,value):
        self.force_dac2_frz_value = value 
        regvalue = self.force_dac2_frz
        # perform operation with reg value 
            
    @property
    def force_dac1_frz(self):
        self.force_dac1_frz_pos   = 5
        self.force_dac1_frz_len   = 1
        return self.force_dac1_frz_value
        
    @force_dac1_frz.setter
    def force_dac1_frz(self,value):
        self.force_dac1_frz_value = value 
        regvalue = self.force_dac1_frz
        # perform operation with reg value 
            
    @property
    def force_dac3_clk_en(self):
        self.force_dac3_clk_en_pos   = 4
        self.force_dac3_clk_en_len   = 1
        return self.force_dac3_clk_en_value
        
    @force_dac3_clk_en.setter
    def force_dac3_clk_en(self,value):
        self.force_dac3_clk_en_value = value 
        regvalue = self.force_dac3_clk_en
        # perform operation with reg value 
            
    @property
    def ref_sdwn_b_dis_m(self):
        self.ref_sdwn_b_dis_m_pos   = 3
        self.ref_sdwn_b_dis_m_len   = 1
        return self.ref_sdwn_b_dis_m_value
        
    @ref_sdwn_b_dis_m.setter
    def ref_sdwn_b_dis_m(self,value):
        self.ref_sdwn_b_dis_m_value = value 
        regvalue = self.ref_sdwn_b_dis_m
        # perform operation with reg value 
            
    @property
    def intfb_en_m(self):
        self.intfb_en_m_pos   = 2
        self.intfb_en_m_len   = 1
        return self.intfb_en_m_value
        
    @intfb_en_m.setter
    def intfb_en_m(self,value):
        self.intfb_en_m_value = value 
        regvalue = self.intfb_en_m
        # perform operation with reg value 
            
    @property
    def pa_pd_d_m(self):
        self.pa_pd_d_m_pos   = 1
        self.pa_pd_d_m_len   = 1
        return self.pa_pd_d_m_value
        
    @pa_pd_d_m.setter
    def pa_pd_d_m(self,value):
        self.pa_pd_d_m_value = value 
        regvalue = self.pa_pd_d_m
        # perform operation with reg value 
            
    @property
    def pa_pd_m(self):
        self.pa_pd_m_pos   = 0
        self.pa_pd_m_len   = 1
        return self.pa_pd_m_value
        
    @pa_pd_m.setter
    def pa_pd_m(self,value):
        self.pa_pd_m_value = value 
        regvalue = self.pa_pd_m
        # perform operation with reg value 
             
class Analog_register_2__Force :
    
    def __init__(self) -> None:
        self.address = 0x11
        self.page = 1
        
    @property
    def bst_bias_m5_0(self):
        self.bst_bias_m5_0_pos   = 0
        self.bst_bias_m5_0_len   = 6
        return self.bst_bias_m5_0_value
        
    @bst_bias_m5_0.setter
    def bst_bias_m5_0(self,value):
        self.bst_bias_m5_0_value = value 
        regvalue = self.bst_bias_m5_0
        # perform operation with reg value 
             
class Analog_register_4__Force :
    
    def __init__(self) -> None:
        self.address = 0x13
        self.page = 1
        
    @property
    def force_pa_clamp_dis(self):
        self.force_pa_clamp_dis_pos   = 7
        self.force_pa_clamp_dis_len   = 1
        return self.force_pa_clamp_dis_value
        
    @force_pa_clamp_dis.setter
    def force_pa_clamp_dis(self,value):
        self.force_pa_clamp_dis_value = value 
        regvalue = self.force_pa_clamp_dis
        # perform operation with reg value 
            
    @property
    def force_fd_res(self):
        self.force_fd_res_pos   = 6
        self.force_fd_res_len   = 1
        return self.force_fd_res_value
        
    @force_fd_res.setter
    def force_fd_res(self,value):
        self.force_fd_res_value = value 
        regvalue = self.force_fd_res
        # perform operation with reg value 
            
    @property
    def force_en_ana_dc_mode(self):
        self.force_en_ana_dc_mode_pos   = 5
        self.force_en_ana_dc_mode_len   = 1
        return self.force_en_ana_dc_mode_value
        
    @force_en_ana_dc_mode.setter
    def force_en_ana_dc_mode(self,value):
        self.force_en_ana_dc_mode_value = value 
        regvalue = self.force_en_ana_dc_mode
        # perform operation with reg value 
            
    @property
    def force_en_dig_path(self):
        self.force_en_dig_path_pos   = 4
        self.force_en_dig_path_len   = 1
        return self.force_en_dig_path_value
        
    @force_en_dig_path.setter
    def force_en_dig_path(self,value):
        self.force_en_dig_path_value = value 
        regvalue = self.force_en_dig_path
        # perform operation with reg value 
            
    @property
    def force_en_ana_path(self):
        self.force_en_ana_path_pos   = 3
        self.force_en_ana_path_len   = 1
        return self.force_en_ana_path_value
        
    @force_en_ana_path.setter
    def force_en_ana_path(self,value):
        self.force_en_ana_path_value = value 
        regvalue = self.force_en_ana_path
        # perform operation with reg value 
            
    @property
    def force_en_dac3(self):
        self.force_en_dac3_pos   = 2
        self.force_en_dac3_len   = 1
        return self.force_en_dac3_value
        
    @force_en_dac3.setter
    def force_en_dac3(self,value):
        self.force_en_dac3_value = value 
        regvalue = self.force_en_dac3
        # perform operation with reg value 
            
    @property
    def force_en_dac2(self):
        self.force_en_dac2_pos   = 1
        self.force_en_dac2_len   = 1
        return self.force_en_dac2_value
        
    @force_en_dac2.setter
    def force_en_dac2(self,value):
        self.force_en_dac2_value = value 
        regvalue = self.force_en_dac2
        # perform operation with reg value 
            
    @property
    def force_en_dac1(self):
        self.force_en_dac1_pos   = 0
        self.force_en_dac1_len   = 1
        return self.force_en_dac1_value
        
    @force_en_dac1.setter
    def force_en_dac1(self,value):
        self.force_en_dac1_value = value 
        regvalue = self.force_en_dac1
        # perform operation with reg value 
             
class Analog_register_5__Force :
    
    def __init__(self) -> None:
        self.address = 0x14
        self.page = 1
        
    @property
    def pa_clamp_dis_m(self):
        self.pa_clamp_dis_m_pos   = 7
        self.pa_clamp_dis_m_len   = 1
        return self.pa_clamp_dis_m_value
        
    @pa_clamp_dis_m.setter
    def pa_clamp_dis_m(self,value):
        self.pa_clamp_dis_m_value = value 
        regvalue = self.pa_clamp_dis_m
        # perform operation with reg value 
            
    @property
    def fd_res_m(self):
        self.fd_res_m_pos   = 6
        self.fd_res_m_len   = 1
        return self.fd_res_m_value
        
    @fd_res_m.setter
    def fd_res_m(self,value):
        self.fd_res_m_value = value 
        regvalue = self.fd_res_m
        # perform operation with reg value 
            
    @property
    def force_bst_fault(self):
        self.force_bst_fault_pos   = 5
        self.force_bst_fault_len   = 1
        return self.force_bst_fault_value
        
    @force_bst_fault.setter
    def force_bst_fault(self,value):
        self.force_bst_fault_value = value 
        regvalue = self.force_bst_fault
        # perform operation with reg value 
            
    @property
    def en_dig_path_m(self):
        self.en_dig_path_m_pos   = 4
        self.en_dig_path_m_len   = 1
        return self.en_dig_path_m_value
        
    @en_dig_path_m.setter
    def en_dig_path_m(self,value):
        self.en_dig_path_m_value = value 
        regvalue = self.en_dig_path_m
        # perform operation with reg value 
            
    @property
    def en_ana_path_m(self):
        self.en_ana_path_m_pos   = 3
        self.en_ana_path_m_len   = 1
        return self.en_ana_path_m_value
        
    @en_ana_path_m.setter
    def en_ana_path_m(self,value):
        self.en_ana_path_m_value = value 
        regvalue = self.en_ana_path_m
        # perform operation with reg value 
            
    @property
    def en_dac3_m(self):
        self.en_dac3_m_pos   = 2
        self.en_dac3_m_len   = 1
        return self.en_dac3_m_value
        
    @en_dac3_m.setter
    def en_dac3_m(self,value):
        self.en_dac3_m_value = value 
        regvalue = self.en_dac3_m
        # perform operation with reg value 
            
    @property
    def en_dac2_m(self):
        self.en_dac2_m_pos   = 1
        self.en_dac2_m_len   = 1
        return self.en_dac2_m_value
        
    @en_dac2_m.setter
    def en_dac2_m(self,value):
        self.en_dac2_m_value = value 
        regvalue = self.en_dac2_m
        # perform operation with reg value 
            
    @property
    def en_dac1_m(self):
        self.en_dac1_m_pos   = 0
        self.en_dac1_m_len   = 1
        return self.en_dac1_m_value
        
    @en_dac1_m.setter
    def en_dac1_m(self,value):
        self.en_dac1_m_value = value 
        regvalue = self.en_dac1_m
        # perform operation with reg value 
             
class Analog_register_6__Force :
    
    def __init__(self) -> None:
        self.address = 0x15
        self.page = 1
        
    @property
    def force_pa_ocp_en(self):
        self.force_pa_ocp_en_pos   = 7
        self.force_pa_ocp_en_len   = 1
        return self.force_pa_ocp_en_value
        
    @force_pa_ocp_en.setter
    def force_pa_ocp_en(self,value):
        self.force_pa_ocp_en_value = value 
        regvalue = self.force_pa_ocp_en
        # perform operation with reg value 
            
    @property
    def force_bst_bat_track_en(self):
        self.force_bst_bat_track_en_pos   = 6
        self.force_bst_bat_track_en_len   = 1
        return self.force_bst_bat_track_en_value
        
    @force_bst_bat_track_en.setter
    def force_bst_bat_track_en(self,value):
        self.force_bst_bat_track_en_value = value 
        regvalue = self.force_bst_bat_track_en
        # perform operation with reg value 
            
    @property
    def force_bst_mfl_en(self):
        self.force_bst_mfl_en_pos   = 5
        self.force_bst_mfl_en_len   = 1
        return self.force_bst_mfl_en_value
        
    @force_bst_mfl_en.setter
    def force_bst_mfl_en(self,value):
        self.force_bst_mfl_en_value = value 
        regvalue = self.force_bst_mfl_en
        # perform operation with reg value 
            
    @property
    def force_bst_en(self):
        self.force_bst_en_pos   = 4
        self.force_bst_en_len   = 1
        return self.force_bst_en_value
        
    @force_bst_en.setter
    def force_bst_en(self,value):
        self.force_bst_en_value = value 
        regvalue = self.force_bst_en
        # perform operation with reg value 
            
    @property
    def force_bst_byp_en(self):
        self.force_bst_byp_en_pos   = 3
        self.force_bst_byp_en_len   = 1
        return self.force_bst_byp_en_value
        
    @force_bst_byp_en.setter
    def force_bst_byp_en(self,value):
        self.force_bst_byp_en_value = value 
        regvalue = self.force_bst_byp_en
        # perform operation with reg value 
            
    @property
    def force_bst_ocp_en(self):
        self.force_bst_ocp_en_pos   = 2
        self.force_bst_ocp_en_len   = 1
        return self.force_bst_ocp_en_value
        
    @force_bst_ocp_en.setter
    def force_bst_ocp_en(self,value):
        self.force_bst_ocp_en_value = value 
        regvalue = self.force_bst_ocp_en
        # perform operation with reg value 
            
    @property
    def force_bst_env_err_en(self):
        self.force_bst_env_err_en_pos   = 1
        self.force_bst_env_err_en_len   = 1
        return self.force_bst_env_err_en_value
        
    @force_bst_env_err_en.setter
    def force_bst_env_err_en(self,value):
        self.force_bst_env_err_en_value = value 
        regvalue = self.force_bst_env_err_en
        # perform operation with reg value 
            
    @property
    def force_bst_env_track_en(self):
        self.force_bst_env_track_en_pos   = 0
        self.force_bst_env_track_en_len   = 1
        return self.force_bst_env_track_en_value
        
    @force_bst_env_track_en.setter
    def force_bst_env_track_en(self,value):
        self.force_bst_env_track_en_value = value 
        regvalue = self.force_bst_env_track_en
        # perform operation with reg value 
             
class Analog_register_7__Force :
    
    def __init__(self) -> None:
        self.address = 0x16
        self.page = 1
        
    @property
    def force_bst_zc_en(self):
        self.force_bst_zc_en_pos   = 7
        self.force_bst_zc_en_len   = 1
        return self.force_bst_zc_en_value
        
    @force_bst_zc_en.setter
    def force_bst_zc_en(self,value):
        self.force_bst_zc_en_value = value 
        regvalue = self.force_bst_zc_en
        # perform operation with reg value 
            
    @property
    def force_bst_bootstrap_en(self):
        self.force_bst_bootstrap_en_pos   = 6
        self.force_bst_bootstrap_en_len   = 1
        return self.force_bst_bootstrap_en_value
        
    @force_bst_bootstrap_en.setter
    def force_bst_bootstrap_en(self,value):
        self.force_bst_bootstrap_en_value = value 
        regvalue = self.force_bst_bootstrap_en
        # perform operation with reg value 
            
    @property
    def force_bst_amp_bias_en(self):
        self.force_bst_amp_bias_en_pos   = 5
        self.force_bst_amp_bias_en_len   = 1
        return self.force_bst_amp_bias_en_value
        
    @force_bst_amp_bias_en.setter
    def force_bst_amp_bias_en(self,value):
        self.force_bst_amp_bias_en_value = value 
        regvalue = self.force_bst_amp_bias_en
        # perform operation with reg value 
            
    @property
    def force_bst_amp_bso_en(self):
        self.force_bst_amp_bso_en_pos   = 4
        self.force_bst_amp_bso_en_len   = 1
        return self.force_bst_amp_bso_en_value
        
    @force_bst_amp_bso_en.setter
    def force_bst_amp_bso_en(self,value):
        self.force_bst_amp_bso_en_value = value 
        regvalue = self.force_bst_amp_bso_en
        # perform operation with reg value 
            
    @property
    def force_bst_comp_bias_en(self):
        self.force_bst_comp_bias_en_pos   = 3
        self.force_bst_comp_bias_en_len   = 1
        return self.force_bst_comp_bias_en_value
        
    @force_bst_comp_bias_en.setter
    def force_bst_comp_bias_en(self,value):
        self.force_bst_comp_bias_en_value = value 
        regvalue = self.force_bst_comp_bias_en
        # perform operation with reg value 
            
    @property
    def force_bst_comp_bso_en(self):
        self.force_bst_comp_bso_en_pos   = 2
        self.force_bst_comp_bso_en_len   = 1
        return self.force_bst_comp_bso_en_value
        
    @force_bst_comp_bso_en.setter
    def force_bst_comp_bso_en(self,value):
        self.force_bst_comp_bso_en_value = value 
        regvalue = self.force_bst_comp_bso_en
        # perform operation with reg value 
            
    @property
    def force_bst_bias_ovp_en(self):
        self.force_bst_bias_ovp_en_pos   = 1
        self.force_bst_bias_ovp_en_len   = 1
        return self.force_bst_bias_ovp_en_value
        
    @force_bst_bias_ovp_en.setter
    def force_bst_bias_ovp_en(self,value):
        self.force_bst_bias_ovp_en_value = value 
        regvalue = self.force_bst_bias_ovp_en
        # perform operation with reg value 
            
    @property
    def force_bst_bso_ovp_en(self):
        self.force_bst_bso_ovp_en_pos   = 0
        self.force_bst_bso_ovp_en_len   = 1
        return self.force_bst_bso_ovp_en_value
        
    @force_bst_bso_ovp_en.setter
    def force_bst_bso_ovp_en(self,value):
        self.force_bst_bso_ovp_en_value = value 
        regvalue = self.force_bst_bso_ovp_en
        # perform operation with reg value 
             
class Analog_register_8__Force :
    
    def __init__(self) -> None:
        self.address = 0x17
        self.page = 1
        
    @property
    def force_dig_fast_charge_cmem(self):
        self.force_dig_fast_charge_cmem_pos   = 7
        self.force_dig_fast_charge_cmem_len   = 1
        return self.force_dig_fast_charge_cmem_value
        
    @force_dig_fast_charge_cmem.setter
    def force_dig_fast_charge_cmem(self,value):
        self.force_dig_fast_charge_cmem_value = value 
        regvalue = self.force_dig_fast_charge_cmem
        # perform operation with reg value 
            
    @property
    def force_dig_bst_mirror_en(self):
        self.force_dig_bst_mirror_en_pos   = 6
        self.force_dig_bst_mirror_en_len   = 1
        return self.force_dig_bst_mirror_en_value
        
    @force_dig_bst_mirror_en.setter
    def force_dig_bst_mirror_en(self,value):
        self.force_dig_bst_mirror_en_value = value 
        regvalue = self.force_dig_bst_mirror_en
        # perform operation with reg value 
            
    @property
    def force_bst_clamp_bias_en(self):
        self.force_bst_clamp_bias_en_pos   = 5
        self.force_bst_clamp_bias_en_len   = 1
        return self.force_bst_clamp_bias_en_value
        
    @force_bst_clamp_bias_en.setter
    def force_bst_clamp_bias_en(self,value):
        self.force_bst_clamp_bias_en_value = value 
        regvalue = self.force_bst_clamp_bias_en
        # perform operation with reg value 
            
    @property
    def force_bst_clamp_bso_en(self):
        self.force_bst_clamp_bso_en_pos   = 4
        self.force_bst_clamp_bso_en_len   = 1
        return self.force_bst_clamp_bso_en_value
        
    @force_bst_clamp_bso_en.setter
    def force_bst_clamp_bso_en(self,value):
        self.force_bst_clamp_bso_en_value = value 
        regvalue = self.force_bst_clamp_bso_en
        # perform operation with reg value 
            
    @property
    def force_dig_azcomp_en_del(self):
        self.force_dig_azcomp_en_del_pos   = 3
        self.force_dig_azcomp_en_del_len   = 1
        return self.force_dig_azcomp_en_del_value
        
    @force_dig_azcomp_en_del.setter
    def force_dig_azcomp_en_del(self,value):
        self.force_dig_azcomp_en_del_value = value 
        regvalue = self.force_dig_azcomp_en_del
        # perform operation with reg value 
            
    @property
    def force_dig_offs_zero_idle(self):
        self.force_dig_offs_zero_idle_pos   = 2
        self.force_dig_offs_zero_idle_len   = 1
        return self.force_dig_offs_zero_idle_value
        
    @force_dig_offs_zero_idle.setter
    def force_dig_offs_zero_idle(self,value):
        self.force_dig_offs_zero_idle_value = value 
        regvalue = self.force_dig_offs_zero_idle
        # perform operation with reg value 
            
    @property
    def force_dig_azcomp_en(self):
        self.force_dig_azcomp_en_pos   = 1
        self.force_dig_azcomp_en_len   = 1
        return self.force_dig_azcomp_en_value
        
    @force_dig_azcomp_en.setter
    def force_dig_azcomp_en(self,value):
        self.force_dig_azcomp_en_value = value 
        regvalue = self.force_dig_azcomp_en
        # perform operation with reg value 
            
    @property
    def force_dig_azcomp_az(self):
        self.force_dig_azcomp_az_pos   = 0
        self.force_dig_azcomp_az_len   = 1
        return self.force_dig_azcomp_az_value
        
    @force_dig_azcomp_az.setter
    def force_dig_azcomp_az(self,value):
        self.force_dig_azcomp_az_value = value 
        regvalue = self.force_dig_azcomp_az
        # perform operation with reg value 
             
class Analog_register_9__Force :
    
    def __init__(self) -> None:
        self.address = 0x18
        self.page = 1
        
    @property
    def dig_fast_charge_cmem_m(self):
        self.dig_fast_charge_cmem_m_pos   = 7
        self.dig_fast_charge_cmem_m_len   = 1
        return self.dig_fast_charge_cmem_m_value
        
    @dig_fast_charge_cmem_m.setter
    def dig_fast_charge_cmem_m(self,value):
        self.dig_fast_charge_cmem_m_value = value 
        regvalue = self.dig_fast_charge_cmem_m
        # perform operation with reg value 
            
    @property
    def dig_bst_mirror_en_m(self):
        self.dig_bst_mirror_en_m_pos   = 6
        self.dig_bst_mirror_en_m_len   = 1
        return self.dig_bst_mirror_en_m_value
        
    @dig_bst_mirror_en_m.setter
    def dig_bst_mirror_en_m(self,value):
        self.dig_bst_mirror_en_m_value = value 
        regvalue = self.dig_bst_mirror_en_m
        # perform operation with reg value 
            
    @property
    def et_datai_unmask(self):
        self.et_datai_unmask_pos   = 5
        self.et_datai_unmask_len   = 1
        return self.et_datai_unmask_value
        
    @et_datai_unmask.setter
    def et_datai_unmask(self,value):
        self.et_datai_unmask_value = value 
        regvalue = self.et_datai_unmask
        # perform operation with reg value 
            
    @property
    def force_pa_nmos_clamp_dis(self):
        self.force_pa_nmos_clamp_dis_pos   = 4
        self.force_pa_nmos_clamp_dis_len   = 1
        return self.force_pa_nmos_clamp_dis_value
        
    @force_pa_nmos_clamp_dis.setter
    def force_pa_nmos_clamp_dis(self,value):
        self.force_pa_nmos_clamp_dis_value = value 
        regvalue = self.force_pa_nmos_clamp_dis
        # perform operation with reg value 
            
    @property
    def dig_azcomp_en_del_m(self):
        self.dig_azcomp_en_del_m_pos   = 3
        self.dig_azcomp_en_del_m_len   = 1
        return self.dig_azcomp_en_del_m_value
        
    @dig_azcomp_en_del_m.setter
    def dig_azcomp_en_del_m(self,value):
        self.dig_azcomp_en_del_m_value = value 
        regvalue = self.dig_azcomp_en_del_m
        # perform operation with reg value 
            
    @property
    def dig_offs_zero_idle_m(self):
        self.dig_offs_zero_idle_m_pos   = 2
        self.dig_offs_zero_idle_m_len   = 1
        return self.dig_offs_zero_idle_m_value
        
    @dig_offs_zero_idle_m.setter
    def dig_offs_zero_idle_m(self,value):
        self.dig_offs_zero_idle_m_value = value 
        regvalue = self.dig_offs_zero_idle_m
        # perform operation with reg value 
            
    @property
    def dig_azcomp_en_m(self):
        self.dig_azcomp_en_m_pos   = 1
        self.dig_azcomp_en_m_len   = 1
        return self.dig_azcomp_en_m_value
        
    @dig_azcomp_en_m.setter
    def dig_azcomp_en_m(self,value):
        self.dig_azcomp_en_m_value = value 
        regvalue = self.dig_azcomp_en_m
        # perform operation with reg value 
            
    @property
    def dig_azcomp_az_m(self):
        self.dig_azcomp_az_m_pos   = 0
        self.dig_azcomp_az_m_len   = 1
        return self.dig_azcomp_az_m_value
        
    @dig_azcomp_az_m.setter
    def dig_azcomp_az_m(self,value):
        self.dig_azcomp_az_m_value = value 
        regvalue = self.dig_azcomp_az_m
        # perform operation with reg value 
             
class Analog_test_1 :
    
    def __init__(self) -> None:
        self.address = 0x19
        self.page = 1
        
    @property
    def ana_tst_mode_en(self):
        self.ana_tst_mode_en_pos   = 7
        self.ana_tst_mode_en_len   = 1
        return self.ana_tst_mode_en_value
        
    @ana_tst_mode_en.setter
    def ana_tst_mode_en(self,value):
        self.ana_tst_mode_en_value = value 
        regvalue = self.ana_tst_mode_en
        # perform operation with reg value 
            
    @property
    def pa_nmos_clamp_dis_m(self):
        self.pa_nmos_clamp_dis_m_pos   = 4
        self.pa_nmos_clamp_dis_m_len   = 1
        return self.pa_nmos_clamp_dis_m_value
        
    @pa_nmos_clamp_dis_m.setter
    def pa_nmos_clamp_dis_m(self,value):
        self.pa_nmos_clamp_dis_m_value = value 
        regvalue = self.pa_nmos_clamp_dis_m
        # perform operation with reg value 
            
    @property
    def azcomp_test_en(self):
        self.azcomp_test_en_pos   = 3
        self.azcomp_test_en_len   = 1
        return self.azcomp_test_en_value
        
    @azcomp_test_en.setter
    def azcomp_test_en(self,value):
        self.azcomp_test_en_value = value 
        regvalue = self.azcomp_test_en
        # perform operation with reg value 
            
    @property
    def dacpa_test_en(self):
        self.dacpa_test_en_pos   = 2
        self.dacpa_test_en_len   = 1
        return self.dacpa_test_en_value
        
    @dacpa_test_en.setter
    def dacpa_test_en(self,value):
        self.dacpa_test_en_value = value 
        regvalue = self.dacpa_test_en
        # perform operation with reg value 
            
    @property
    def bst_test_en(self):
        self.bst_test_en_pos   = 1
        self.bst_test_en_len   = 1
        return self.bst_test_en_value
        
    @bst_test_en.setter
    def bst_test_en(self,value):
        self.bst_test_en_value = value 
        regvalue = self.bst_test_en
        # perform operation with reg value 
            
    @property
    def ref_test_en(self):
        self.ref_test_en_pos   = 0
        self.ref_test_en_len   = 1
        return self.ref_test_en_value
        
    @ref_test_en.setter
    def ref_test_en(self,value):
        self.ref_test_en_value = value 
        regvalue = self.ref_test_en
        # perform operation with reg value 
             
class Analog_test_2 :
    
    def __init__(self) -> None:
        self.address = 0x1a
        self.page = 1
        
    @property
    def ana_test_sel7_0(self):
        self.ana_test_sel7_0_pos   = 0
        self.ana_test_sel7_0_len   = 8
        return self.ana_test_sel7_0_value
        
    @ana_test_sel7_0.setter
    def ana_test_sel7_0(self,value):
        self.ana_test_sel7_0_value = value 
        regvalue = self.ana_test_sel7_0
        # perform operation with reg value 
             
class Internal_sin_register_1 :
    
    def __init__(self) -> None:
        self.address = 0x1e
        self.page = 1
        
    @property
    def internal_sin_gain3_0(self):
        self.internal_sin_gain3_0_pos   = 4
        self.internal_sin_gain3_0_len   = 4
        return self.internal_sin_gain3_0_value
        
    @internal_sin_gain3_0.setter
    def internal_sin_gain3_0(self,value):
        self.internal_sin_gain3_0_value = value 
        regvalue = self.internal_sin_gain3_0
        # perform operation with reg value 
            
    @property
    def internal_sin_en(self):
        self.internal_sin_en_pos   = 3
        self.internal_sin_en_len   = 1
        return self.internal_sin_en_value
        
    @internal_sin_en.setter
    def internal_sin_en(self,value):
        self.internal_sin_en_value = value 
        regvalue = self.internal_sin_en
        # perform operation with reg value 
            
    @property
    def internal_sin_freq2_0(self):
        self.internal_sin_freq2_0_pos   = 0
        self.internal_sin_freq2_0_len   = 3
        return self.internal_sin_freq2_0_value
        
    @internal_sin_freq2_0.setter
    def internal_sin_freq2_0(self,value):
        self.internal_sin_freq2_0_value = value 
        regvalue = self.internal_sin_freq2_0
        # perform operation with reg value 
             
class Internal_sin_register_2 :
    
    def __init__(self) -> None:
        self.address = 0x1f
        self.page = 1
        
    @property
    def internal_sin_offset7_0(self):
        self.internal_sin_offset7_0_pos   = 0
        self.internal_sin_offset7_0_len   = 8
        return self.internal_sin_offset7_0_value
        
    @internal_sin_offset7_0.setter
    def internal_sin_offset7_0(self,value):
        self.internal_sin_offset7_0_value = value 
        regvalue = self.internal_sin_offset7_0
        # perform operation with reg value 
             
class Debug_resgister_1 :
    
    def __init__(self) -> None:
        self.address = 0x20
        self.page = 1
        
    @property
    def debug_in_en8(self):
        self.debug_in_en8_pos   = 0
        self.debug_in_en8_len   = 1
        return self.debug_in_en8_value
        
    @debug_in_en8.setter
    def debug_in_en8(self,value):
        self.debug_in_en8_value = value 
        regvalue = self.debug_in_en8
        # perform operation with reg value 
             
class Debug_resgister_2 :
    
    def __init__(self) -> None:
        self.address = 0x21
        self.page = 1
        
    @property
    def debug_in_en7_0(self):
        self.debug_in_en7_0_pos   = 0
        self.debug_in_en7_0_len   = 8
        return self.debug_in_en7_0_value
        
    @debug_in_en7_0.setter
    def debug_in_en7_0(self,value):
        self.debug_in_en7_0_value = value 
        regvalue = self.debug_in_en7_0
        # perform operation with reg value 
             
class Debug_resgister_3 :
    
    def __init__(self) -> None:
        self.address = 0x22
        self.page = 1
        
    @property
    def debug_in8(self):
        self.debug_in8_pos   = 0
        self.debug_in8_len   = 1
        return self.debug_in8_value
        
    @debug_in8.setter
    def debug_in8(self,value):
        self.debug_in8_value = value 
        regvalue = self.debug_in8
        # perform operation with reg value 
             
class Debug_resgister_4 :
    
    def __init__(self) -> None:
        self.address = 0x23
        self.page = 1
        
    @property
    def debug_in7_0(self):
        self.debug_in7_0_pos   = 0
        self.debug_in7_0_len   = 8
        return self.debug_in7_0_value
        
    @debug_in7_0.setter
    def debug_in7_0(self,value):
        self.debug_in7_0_value = value 
        regvalue = self.debug_in7_0
        # perform operation with reg value 
             
class Debug_resgister_5 :
    
    def __init__(self) -> None:
        self.address = 0x24
        self.page = 1
        
    @property
    def debug_en(self):
        self.debug_en_pos   = 0
        self.debug_en_len   = 1
        return self.debug_en_value
        
    @debug_en.setter
    def debug_en(self,value):
        self.debug_en_value = value 
        regvalue = self.debug_en
        # perform operation with reg value 
             
class UNCLOCK_REGISTER :
    
    def __init__(self) -> None:
        self.address = 0x2f
        self.page = 1
        
    @property
    def unlock_tst_addr(self):
        self.unlock_tst_addr_pos   = 0
        self.unlock_tst_addr_len   = 1
        return self.unlock_tst_addr_value
        
    @unlock_tst_addr.setter
    def unlock_tst_addr(self,value):
        self.unlock_tst_addr_value = value 
        regvalue = self.unlock_tst_addr
        # perform operation with reg value 
             
class IFIR_CONFIG_1 :
    
    def __init__(self) -> None:
        self.address = 0x30
        self.page = 1
        
    @property
    def ifir_coeff_nr1_0(self):
        self.ifir_coeff_nr1_0_pos   = 6
        self.ifir_coeff_nr1_0_len   = 2
        return self.ifir_coeff_nr1_0_value
        
    @ifir_coeff_nr1_0.setter
    def ifir_coeff_nr1_0(self,value):
        self.ifir_coeff_nr1_0_value = value 
        regvalue = self.ifir_coeff_nr1_0
        # perform operation with reg value 
            
    @property
    def ifir_mode1_0(self):
        self.ifir_mode1_0_pos   = 4
        self.ifir_mode1_0_len   = 2
        return self.ifir_mode1_0_value
        
    @ifir_mode1_0.setter
    def ifir_mode1_0(self,value):
        self.ifir_mode1_0_value = value 
        regvalue = self.ifir_mode1_0
        # perform operation with reg value 
            
    @property
    def ifir_shift3_0(self):
        self.ifir_shift3_0_pos   = 0
        self.ifir_shift3_0_len   = 4
        return self.ifir_shift3_0_value
        
    @ifir_shift3_0.setter
    def ifir_shift3_0(self,value):
        self.ifir_shift3_0_value = value 
        regvalue = self.ifir_shift3_0
        # perform operation with reg value 
             
class IFIR_CONFIG_2 :
    
    def __init__(self) -> None:
        self.address = 0x31
        self.page = 1
        
    @property
    def ifir_coeff_loader_start(self):
        self.ifir_coeff_loader_start_pos   = 0
        self.ifir_coeff_loader_start_len   = 1
        return self.ifir_coeff_loader_start_value
        
    @ifir_coeff_loader_start.setter
    def ifir_coeff_loader_start(self,value):
        self.ifir_coeff_loader_start_value = value 
        regvalue = self.ifir_coeff_loader_start
        # perform operation with reg value 
             
class IFIR_COEFF_0_MSB :
    
    def __init__(self) -> None:
        self.address = 0x32
        self.page = 1
        
    @property
    def ifir_coeff_09_8(self):
        self.ifir_coeff_09_8_pos   = 0
        self.ifir_coeff_09_8_len   = 2
        return self.ifir_coeff_09_8_value
        
    @ifir_coeff_09_8.setter
    def ifir_coeff_09_8(self,value):
        self.ifir_coeff_09_8_value = value 
        regvalue = self.ifir_coeff_09_8
        # perform operation with reg value 
             
class IFIR_COEFF_0_LSB :
    
    def __init__(self) -> None:
        self.address = 0x33
        self.page = 1
        
    @property
    def ifir_coeff_07_0(self):
        self.ifir_coeff_07_0_pos   = 0
        self.ifir_coeff_07_0_len   = 8
        return self.ifir_coeff_07_0_value
        
    @ifir_coeff_07_0.setter
    def ifir_coeff_07_0(self,value):
        self.ifir_coeff_07_0_value = value 
        regvalue = self.ifir_coeff_07_0
        # perform operation with reg value 
             
class IFIR_COEFF_1_MSB :
    
    def __init__(self) -> None:
        self.address = 0x34
        self.page = 1
        
    @property
    def ifir_coeff_19_8(self):
        self.ifir_coeff_19_8_pos   = 0
        self.ifir_coeff_19_8_len   = 2
        return self.ifir_coeff_19_8_value
        
    @ifir_coeff_19_8.setter
    def ifir_coeff_19_8(self,value):
        self.ifir_coeff_19_8_value = value 
        regvalue = self.ifir_coeff_19_8
        # perform operation with reg value 
             
class IFIR_COEFF_1_LSB :
    
    def __init__(self) -> None:
        self.address = 0x35
        self.page = 1
        
    @property
    def ifir_coeff_17_0(self):
        self.ifir_coeff_17_0_pos   = 0
        self.ifir_coeff_17_0_len   = 8
        return self.ifir_coeff_17_0_value
        
    @ifir_coeff_17_0.setter
    def ifir_coeff_17_0(self,value):
        self.ifir_coeff_17_0_value = value 
        regvalue = self.ifir_coeff_17_0
        # perform operation with reg value 
             
class IFIR_COEFF_2_MSB :
    
    def __init__(self) -> None:
        self.address = 0x36
        self.page = 1
        
    @property
    def ifir_coeff_29_8(self):
        self.ifir_coeff_29_8_pos   = 0
        self.ifir_coeff_29_8_len   = 2
        return self.ifir_coeff_29_8_value
        
    @ifir_coeff_29_8.setter
    def ifir_coeff_29_8(self,value):
        self.ifir_coeff_29_8_value = value 
        regvalue = self.ifir_coeff_29_8
        # perform operation with reg value 
             
class IFIR_COEFF_2_LSB :
    
    def __init__(self) -> None:
        self.address = 0x37
        self.page = 1
        
    @property
    def ifir_coeff_27_0(self):
        self.ifir_coeff_27_0_pos   = 0
        self.ifir_coeff_27_0_len   = 8
        return self.ifir_coeff_27_0_value
        
    @ifir_coeff_27_0.setter
    def ifir_coeff_27_0(self,value):
        self.ifir_coeff_27_0_value = value 
        regvalue = self.ifir_coeff_27_0
        # perform operation with reg value 
             
class IFIR_COEFF_3_MSB :
    
    def __init__(self) -> None:
        self.address = 0x38
        self.page = 1
        
    @property
    def ifir_coeff_39_8(self):
        self.ifir_coeff_39_8_pos   = 0
        self.ifir_coeff_39_8_len   = 2
        return self.ifir_coeff_39_8_value
        
    @ifir_coeff_39_8.setter
    def ifir_coeff_39_8(self,value):
        self.ifir_coeff_39_8_value = value 
        regvalue = self.ifir_coeff_39_8
        # perform operation with reg value 
             
class IFIR_COEFF_3_LSB :
    
    def __init__(self) -> None:
        self.address = 0x39
        self.page = 1
        
    @property
    def ifir_coeff_37_0(self):
        self.ifir_coeff_37_0_pos   = 0
        self.ifir_coeff_37_0_len   = 8
        return self.ifir_coeff_37_0_value
        
    @ifir_coeff_37_0.setter
    def ifir_coeff_37_0(self,value):
        self.ifir_coeff_37_0_value = value 
        regvalue = self.ifir_coeff_37_0
        # perform operation with reg value 
             
class IFIR_COEFF_4_MSB :
    
    def __init__(self) -> None:
        self.address = 0x3a
        self.page = 1
        
    @property
    def ifir_coeff_49_8(self):
        self.ifir_coeff_49_8_pos   = 0
        self.ifir_coeff_49_8_len   = 2
        return self.ifir_coeff_49_8_value
        
    @ifir_coeff_49_8.setter
    def ifir_coeff_49_8(self,value):
        self.ifir_coeff_49_8_value = value 
        regvalue = self.ifir_coeff_49_8
        # perform operation with reg value 
             
class IFIR_COEFF_4_LSB :
    
    def __init__(self) -> None:
        self.address = 0x3b
        self.page = 1
        
    @property
    def ifir_coeff_47_0(self):
        self.ifir_coeff_47_0_pos   = 0
        self.ifir_coeff_47_0_len   = 8
        return self.ifir_coeff_47_0_value
        
    @ifir_coeff_47_0.setter
    def ifir_coeff_47_0(self,value):
        self.ifir_coeff_47_0_value = value 
        regvalue = self.ifir_coeff_47_0
        # perform operation with reg value 
             
class IFIR_COEFF_5_MSB :
    
    def __init__(self) -> None:
        self.address = 0x3c
        self.page = 1
        
    @property
    def ifir_coeff_59_8(self):
        self.ifir_coeff_59_8_pos   = 0
        self.ifir_coeff_59_8_len   = 2
        return self.ifir_coeff_59_8_value
        
    @ifir_coeff_59_8.setter
    def ifir_coeff_59_8(self,value):
        self.ifir_coeff_59_8_value = value 
        regvalue = self.ifir_coeff_59_8
        # perform operation with reg value 
             
class IFIR_COEFF_5_LSB :
    
    def __init__(self) -> None:
        self.address = 0x3d
        self.page = 1
        
    @property
    def ifir_coeff_57_0(self):
        self.ifir_coeff_57_0_pos   = 0
        self.ifir_coeff_57_0_len   = 8
        return self.ifir_coeff_57_0_value
        
    @ifir_coeff_57_0.setter
    def ifir_coeff_57_0(self,value):
        self.ifir_coeff_57_0_value = value 
        regvalue = self.ifir_coeff_57_0
        # perform operation with reg value 
             
class IFIR_COEFF_6_MSB :
    
    def __init__(self) -> None:
        self.address = 0x3e
        self.page = 1
        
    @property
    def ifir_coeff_69_8(self):
        self.ifir_coeff_69_8_pos   = 0
        self.ifir_coeff_69_8_len   = 2
        return self.ifir_coeff_69_8_value
        
    @ifir_coeff_69_8.setter
    def ifir_coeff_69_8(self,value):
        self.ifir_coeff_69_8_value = value 
        regvalue = self.ifir_coeff_69_8
        # perform operation with reg value 
             
class IFIR_COEFF_6_LSB :
    
    def __init__(self) -> None:
        self.address = 0x3f
        self.page = 1
        
    @property
    def ifir_coeff_67_0(self):
        self.ifir_coeff_67_0_pos   = 0
        self.ifir_coeff_67_0_len   = 8
        return self.ifir_coeff_67_0_value
        
    @ifir_coeff_67_0.setter
    def ifir_coeff_67_0(self,value):
        self.ifir_coeff_67_0_value = value 
        regvalue = self.ifir_coeff_67_0
        # perform operation with reg value 
             
class IFIR_COEFF_7_MSB :
    
    def __init__(self) -> None:
        self.address = 0x40
        self.page = 1
        
    @property
    def ifir_coeff_79_8(self):
        self.ifir_coeff_79_8_pos   = 0
        self.ifir_coeff_79_8_len   = 2
        return self.ifir_coeff_79_8_value
        
    @ifir_coeff_79_8.setter
    def ifir_coeff_79_8(self,value):
        self.ifir_coeff_79_8_value = value 
        regvalue = self.ifir_coeff_79_8
        # perform operation with reg value 
             
class IFIR_COEFF_7_LSB :
    
    def __init__(self) -> None:
        self.address = 0x41
        self.page = 1
        
    @property
    def ifir_coeff_77_0(self):
        self.ifir_coeff_77_0_pos   = 0
        self.ifir_coeff_77_0_len   = 8
        return self.ifir_coeff_77_0_value
        
    @ifir_coeff_77_0.setter
    def ifir_coeff_77_0(self,value):
        self.ifir_coeff_77_0_value = value 
        regvalue = self.ifir_coeff_77_0
        # perform operation with reg value 
             
class IFIR_COEFF_8_MSB :
    
    def __init__(self) -> None:
        self.address = 0x42
        self.page = 1
        
    @property
    def ifir_coeff_89_8(self):
        self.ifir_coeff_89_8_pos   = 0
        self.ifir_coeff_89_8_len   = 2
        return self.ifir_coeff_89_8_value
        
    @ifir_coeff_89_8.setter
    def ifir_coeff_89_8(self,value):
        self.ifir_coeff_89_8_value = value 
        regvalue = self.ifir_coeff_89_8
        # perform operation with reg value 
             
class IFIR_COEFF_8_LSB :
    
    def __init__(self) -> None:
        self.address = 0x43
        self.page = 1
        
    @property
    def ifir_coeff_87_0(self):
        self.ifir_coeff_87_0_pos   = 0
        self.ifir_coeff_87_0_len   = 8
        return self.ifir_coeff_87_0_value
        
    @ifir_coeff_87_0.setter
    def ifir_coeff_87_0(self,value):
        self.ifir_coeff_87_0_value = value 
        regvalue = self.ifir_coeff_87_0
        # perform operation with reg value 
             
class IFIR_COEFF_9_MSB :
    
    def __init__(self) -> None:
        self.address = 0x44
        self.page = 1
        
    @property
    def ifir_coeff_99_8(self):
        self.ifir_coeff_99_8_pos   = 0
        self.ifir_coeff_99_8_len   = 2
        return self.ifir_coeff_99_8_value
        
    @ifir_coeff_99_8.setter
    def ifir_coeff_99_8(self,value):
        self.ifir_coeff_99_8_value = value 
        regvalue = self.ifir_coeff_99_8
        # perform operation with reg value 
             
class IFIR_COEFF_9_LSB :
    
    def __init__(self) -> None:
        self.address = 0x45
        self.page = 1
        
    @property
    def ifir_coeff_97_0(self):
        self.ifir_coeff_97_0_pos   = 0
        self.ifir_coeff_97_0_len   = 8
        return self.ifir_coeff_97_0_value
        
    @ifir_coeff_97_0.setter
    def ifir_coeff_97_0(self,value):
        self.ifir_coeff_97_0_value = value 
        regvalue = self.ifir_coeff_97_0
        # perform operation with reg value 
             
class IFIR_COEFF_10_MSB :
    
    def __init__(self) -> None:
        self.address = 0x46
        self.page = 1
        
    @property
    def ifir_coeff_109_8(self):
        self.ifir_coeff_109_8_pos   = 0
        self.ifir_coeff_109_8_len   = 2
        return self.ifir_coeff_109_8_value
        
    @ifir_coeff_109_8.setter
    def ifir_coeff_109_8(self,value):
        self.ifir_coeff_109_8_value = value 
        regvalue = self.ifir_coeff_109_8
        # perform operation with reg value 
             
class IFIR_COEFF_10_LSB :
    
    def __init__(self) -> None:
        self.address = 0x47
        self.page = 1
        
    @property
    def ifir_coeff_107_0(self):
        self.ifir_coeff_107_0_pos   = 0
        self.ifir_coeff_107_0_len   = 8
        return self.ifir_coeff_107_0_value
        
    @ifir_coeff_107_0.setter
    def ifir_coeff_107_0(self,value):
        self.ifir_coeff_107_0_value = value 
        regvalue = self.ifir_coeff_107_0
        # perform operation with reg value 
             
class IFIR_COEFF_11_MSB :
    
    def __init__(self) -> None:
        self.address = 0x48
        self.page = 1
        
    @property
    def ifir_coeff_119_8(self):
        self.ifir_coeff_119_8_pos   = 0
        self.ifir_coeff_119_8_len   = 2
        return self.ifir_coeff_119_8_value
        
    @ifir_coeff_119_8.setter
    def ifir_coeff_119_8(self,value):
        self.ifir_coeff_119_8_value = value 
        regvalue = self.ifir_coeff_119_8
        # perform operation with reg value 
             
class IFIR_COEFF_11_LSB :
    
    def __init__(self) -> None:
        self.address = 0x49
        self.page = 1
        
    @property
    def ifir_coeff_117_0(self):
        self.ifir_coeff_117_0_pos   = 0
        self.ifir_coeff_117_0_len   = 8
        return self.ifir_coeff_117_0_value
        
    @ifir_coeff_117_0.setter
    def ifir_coeff_117_0(self,value):
        self.ifir_coeff_117_0_value = value 
        regvalue = self.ifir_coeff_117_0
        # perform operation with reg value 
             
class IFIR_COEFF_12_MSB :
    
    def __init__(self) -> None:
        self.address = 0x4a
        self.page = 1
        
    @property
    def ifir_coeff_129_8(self):
        self.ifir_coeff_129_8_pos   = 0
        self.ifir_coeff_129_8_len   = 2
        return self.ifir_coeff_129_8_value
        
    @ifir_coeff_129_8.setter
    def ifir_coeff_129_8(self,value):
        self.ifir_coeff_129_8_value = value 
        regvalue = self.ifir_coeff_129_8
        # perform operation with reg value 
             
class IFIR_COEFF_12_LSB :
    
    def __init__(self) -> None:
        self.address = 0x4b
        self.page = 1
        
    @property
    def ifir_coeff_127_0(self):
        self.ifir_coeff_127_0_pos   = 0
        self.ifir_coeff_127_0_len   = 8
        return self.ifir_coeff_127_0_value
        
    @ifir_coeff_127_0.setter
    def ifir_coeff_127_0(self,value):
        self.ifir_coeff_127_0_value = value 
        regvalue = self.ifir_coeff_127_0
        # perform operation with reg value 
             
class IFIR_COEFF_13_MSB :
    
    def __init__(self) -> None:
        self.address = 0x4c
        self.page = 1
        
    @property
    def ifir_coeff_139_8(self):
        self.ifir_coeff_139_8_pos   = 0
        self.ifir_coeff_139_8_len   = 2
        return self.ifir_coeff_139_8_value
        
    @ifir_coeff_139_8.setter
    def ifir_coeff_139_8(self,value):
        self.ifir_coeff_139_8_value = value 
        regvalue = self.ifir_coeff_139_8
        # perform operation with reg value 
             
class IFIR_COEFF_13_LSB :
    
    def __init__(self) -> None:
        self.address = 0x4d
        self.page = 1
        
    @property
    def ifir_coeff_137_0(self):
        self.ifir_coeff_137_0_pos   = 0
        self.ifir_coeff_137_0_len   = 8
        return self.ifir_coeff_137_0_value
        
    @ifir_coeff_137_0.setter
    def ifir_coeff_137_0(self,value):
        self.ifir_coeff_137_0_value = value 
        regvalue = self.ifir_coeff_137_0
        # perform operation with reg value 
             
class IFIR_COEFF_14_MSB :
    
    def __init__(self) -> None:
        self.address = 0x4e
        self.page = 1
        
    @property
    def ifir_coeff_149_8(self):
        self.ifir_coeff_149_8_pos   = 0
        self.ifir_coeff_149_8_len   = 2
        return self.ifir_coeff_149_8_value
        
    @ifir_coeff_149_8.setter
    def ifir_coeff_149_8(self,value):
        self.ifir_coeff_149_8_value = value 
        regvalue = self.ifir_coeff_149_8
        # perform operation with reg value 
             
class IFIR_COEFF_14_LSB :
    
    def __init__(self) -> None:
        self.address = 0x4f
        self.page = 1
        
    @property
    def ifir_coeff_147_0(self):
        self.ifir_coeff_147_0_pos   = 0
        self.ifir_coeff_147_0_len   = 8
        return self.ifir_coeff_147_0_value
        
    @ifir_coeff_147_0.setter
    def ifir_coeff_147_0(self,value):
        self.ifir_coeff_147_0_value = value 
        regvalue = self.ifir_coeff_147_0
        # perform operation with reg value 
             
class IFIR_COEFF_15_MSB :
    
    def __init__(self) -> None:
        self.address = 0x50
        self.page = 1
        
    @property
    def ifir_coeff_159_8(self):
        self.ifir_coeff_159_8_pos   = 0
        self.ifir_coeff_159_8_len   = 2
        return self.ifir_coeff_159_8_value
        
    @ifir_coeff_159_8.setter
    def ifir_coeff_159_8(self,value):
        self.ifir_coeff_159_8_value = value 
        regvalue = self.ifir_coeff_159_8
        # perform operation with reg value 
             
class IFIR_COEFF_15_LSB :
    
    def __init__(self) -> None:
        self.address = 0x51
        self.page = 1
        
    @property
    def ifir_coeff_157_0(self):
        self.ifir_coeff_157_0_pos   = 0
        self.ifir_coeff_157_0_len   = 8
        return self.ifir_coeff_157_0_value
        
    @ifir_coeff_157_0.setter
    def ifir_coeff_157_0(self,value):
        self.ifir_coeff_157_0_value = value 
        regvalue = self.ifir_coeff_157_0
        # perform operation with reg value 
             
class IFIR_COEFF_16_MSB :
    
    def __init__(self) -> None:
        self.address = 0x52
        self.page = 1
        
    @property
    def ifir_coeff_169_8(self):
        self.ifir_coeff_169_8_pos   = 0
        self.ifir_coeff_169_8_len   = 2
        return self.ifir_coeff_169_8_value
        
    @ifir_coeff_169_8.setter
    def ifir_coeff_169_8(self,value):
        self.ifir_coeff_169_8_value = value 
        regvalue = self.ifir_coeff_169_8
        # perform operation with reg value 
             
class IFIR_COEFF_16_LSB :
    
    def __init__(self) -> None:
        self.address = 0x53
        self.page = 1
        
    @property
    def ifir_coeff_167_0(self):
        self.ifir_coeff_167_0_pos   = 0
        self.ifir_coeff_167_0_len   = 8
        return self.ifir_coeff_167_0_value
        
    @ifir_coeff_167_0.setter
    def ifir_coeff_167_0(self,value):
        self.ifir_coeff_167_0_value = value 
        regvalue = self.ifir_coeff_167_0
        # perform operation with reg value 
             
class IFIR_COEFF_17_MSB :
    
    def __init__(self) -> None:
        self.address = 0x54
        self.page = 1
        
    @property
    def ifir_coeff_179_8(self):
        self.ifir_coeff_179_8_pos   = 0
        self.ifir_coeff_179_8_len   = 2
        return self.ifir_coeff_179_8_value
        
    @ifir_coeff_179_8.setter
    def ifir_coeff_179_8(self,value):
        self.ifir_coeff_179_8_value = value 
        regvalue = self.ifir_coeff_179_8
        # perform operation with reg value 
             
class IFIR_COEFF_17_LSB :
    
    def __init__(self) -> None:
        self.address = 0x55
        self.page = 1
        
    @property
    def ifir_coeff_177_0(self):
        self.ifir_coeff_177_0_pos   = 0
        self.ifir_coeff_177_0_len   = 8
        return self.ifir_coeff_177_0_value
        
    @ifir_coeff_177_0.setter
    def ifir_coeff_177_0(self,value):
        self.ifir_coeff_177_0_value = value 
        regvalue = self.ifir_coeff_177_0
        # perform operation with reg value 
             
class IFIR_COEFF_18_MSB :
    
    def __init__(self) -> None:
        self.address = 0x56
        self.page = 1
        
    @property
    def ifir_coeff_189_8(self):
        self.ifir_coeff_189_8_pos   = 0
        self.ifir_coeff_189_8_len   = 2
        return self.ifir_coeff_189_8_value
        
    @ifir_coeff_189_8.setter
    def ifir_coeff_189_8(self,value):
        self.ifir_coeff_189_8_value = value 
        regvalue = self.ifir_coeff_189_8
        # perform operation with reg value 
             
class IFIR_COEFF_18_LSB :
    
    def __init__(self) -> None:
        self.address = 0x57
        self.page = 1
        
    @property
    def ifir_coeff_187_0(self):
        self.ifir_coeff_187_0_pos   = 0
        self.ifir_coeff_187_0_len   = 8
        return self.ifir_coeff_187_0_value
        
    @ifir_coeff_187_0.setter
    def ifir_coeff_187_0(self,value):
        self.ifir_coeff_187_0_value = value 
        regvalue = self.ifir_coeff_187_0
        # perform operation with reg value 
             
class IFIR_COEFF_19_MSB :
    
    def __init__(self) -> None:
        self.address = 0x58
        self.page = 1
        
    @property
    def ifir_coeff_199_8(self):
        self.ifir_coeff_199_8_pos   = 0
        self.ifir_coeff_199_8_len   = 2
        return self.ifir_coeff_199_8_value
        
    @ifir_coeff_199_8.setter
    def ifir_coeff_199_8(self,value):
        self.ifir_coeff_199_8_value = value 
        regvalue = self.ifir_coeff_199_8
        # perform operation with reg value 
             
class IFIR_COEFF_19_LSB :
    
    def __init__(self) -> None:
        self.address = 0x59
        self.page = 1
        
    @property
    def ifir_coeff_197_0(self):
        self.ifir_coeff_197_0_pos   = 0
        self.ifir_coeff_197_0_len   = 8
        return self.ifir_coeff_197_0_value
        
    @ifir_coeff_197_0.setter
    def ifir_coeff_197_0(self,value):
        self.ifir_coeff_197_0_value = value 
        regvalue = self.ifir_coeff_197_0
        # perform operation with reg value 
             
class IFIR_COEFF_20_MSB :
    
    def __init__(self) -> None:
        self.address = 0x5a
        self.page = 1
        
    @property
    def ifir_coeff_209_8(self):
        self.ifir_coeff_209_8_pos   = 0
        self.ifir_coeff_209_8_len   = 2
        return self.ifir_coeff_209_8_value
        
    @ifir_coeff_209_8.setter
    def ifir_coeff_209_8(self,value):
        self.ifir_coeff_209_8_value = value 
        regvalue = self.ifir_coeff_209_8
        # perform operation with reg value 
             
class IFIR_COEFF_20_LSB :
    
    def __init__(self) -> None:
        self.address = 0x5b
        self.page = 1
        
    @property
    def ifir_coeff_207_0(self):
        self.ifir_coeff_207_0_pos   = 0
        self.ifir_coeff_207_0_len   = 8
        return self.ifir_coeff_207_0_value
        
    @ifir_coeff_207_0.setter
    def ifir_coeff_207_0(self,value):
        self.ifir_coeff_207_0_value = value 
        regvalue = self.ifir_coeff_207_0
        # perform operation with reg value 
             
class IFIR_COEFF_21_MSB :
    
    def __init__(self) -> None:
        self.address = 0x5c
        self.page = 1
        
    @property
    def ifir_coeff_219_8(self):
        self.ifir_coeff_219_8_pos   = 0
        self.ifir_coeff_219_8_len   = 2
        return self.ifir_coeff_219_8_value
        
    @ifir_coeff_219_8.setter
    def ifir_coeff_219_8(self,value):
        self.ifir_coeff_219_8_value = value 
        regvalue = self.ifir_coeff_219_8
        # perform operation with reg value 
             
class IFIR_COEFF_21_LSB :
    
    def __init__(self) -> None:
        self.address = 0x5d
        self.page = 1
        
    @property
    def ifir_coeff_217_0(self):
        self.ifir_coeff_217_0_pos   = 0
        self.ifir_coeff_217_0_len   = 8
        return self.ifir_coeff_217_0_value
        
    @ifir_coeff_217_0.setter
    def ifir_coeff_217_0(self,value):
        self.ifir_coeff_217_0_value = value 
        regvalue = self.ifir_coeff_217_0
        # perform operation with reg value 
             
class IFIR_COEFF_22_MSB :
    
    def __init__(self) -> None:
        self.address = 0x5e
        self.page = 1
        
    @property
    def ifir_coeff_229_8(self):
        self.ifir_coeff_229_8_pos   = 0
        self.ifir_coeff_229_8_len   = 2
        return self.ifir_coeff_229_8_value
        
    @ifir_coeff_229_8.setter
    def ifir_coeff_229_8(self,value):
        self.ifir_coeff_229_8_value = value 
        regvalue = self.ifir_coeff_229_8
        # perform operation with reg value 
             
class IFIR_COEFF_22_LSB :
    
    def __init__(self) -> None:
        self.address = 0x5f
        self.page = 1
        
    @property
    def ifir_coeff_227_0(self):
        self.ifir_coeff_227_0_pos   = 0
        self.ifir_coeff_227_0_len   = 8
        return self.ifir_coeff_227_0_value
        
    @ifir_coeff_227_0.setter
    def ifir_coeff_227_0(self,value):
        self.ifir_coeff_227_0_value = value 
        regvalue = self.ifir_coeff_227_0
        # perform operation with reg value 
             
class IFIR_COEFF_23_MSB :
    
    def __init__(self) -> None:
        self.address = 0x60
        self.page = 1
        
    @property
    def ifir_coeff_239_8(self):
        self.ifir_coeff_239_8_pos   = 0
        self.ifir_coeff_239_8_len   = 2
        return self.ifir_coeff_239_8_value
        
    @ifir_coeff_239_8.setter
    def ifir_coeff_239_8(self,value):
        self.ifir_coeff_239_8_value = value 
        regvalue = self.ifir_coeff_239_8
        # perform operation with reg value 
             
class IFIR_COEFF_23_LSB :
    
    def __init__(self) -> None:
        self.address = 0x61
        self.page = 1
        
    @property
    def ifir_coeff_237_0(self):
        self.ifir_coeff_237_0_pos   = 0
        self.ifir_coeff_237_0_len   = 8
        return self.ifir_coeff_237_0_value
        
    @ifir_coeff_237_0.setter
    def ifir_coeff_237_0(self,value):
        self.ifir_coeff_237_0_value = value 
        regvalue = self.ifir_coeff_237_0
        # perform operation with reg value 
             
class IFIR_COEFF_24_MSB :
    
    def __init__(self) -> None:
        self.address = 0x62
        self.page = 1
        
    @property
    def ifir_coeff_249_8(self):
        self.ifir_coeff_249_8_pos   = 0
        self.ifir_coeff_249_8_len   = 2
        return self.ifir_coeff_249_8_value
        
    @ifir_coeff_249_8.setter
    def ifir_coeff_249_8(self,value):
        self.ifir_coeff_249_8_value = value 
        regvalue = self.ifir_coeff_249_8
        # perform operation with reg value 
             
class IFIR_COEFF_24_LSB :
    
    def __init__(self) -> None:
        self.address = 0x63
        self.page = 1
        
    @property
    def ifir_coeff_247_0(self):
        self.ifir_coeff_247_0_pos   = 0
        self.ifir_coeff_247_0_len   = 8
        return self.ifir_coeff_247_0_value
        
    @ifir_coeff_247_0.setter
    def ifir_coeff_247_0(self,value):
        self.ifir_coeff_247_0_value = value 
        regvalue = self.ifir_coeff_247_0
        # perform operation with reg value 
             
class IFIR_COEFF_25_MSB :
    
    def __init__(self) -> None:
        self.address = 0x64
        self.page = 1
        
    @property
    def ifir_coeff_259_8(self):
        self.ifir_coeff_259_8_pos   = 0
        self.ifir_coeff_259_8_len   = 2
        return self.ifir_coeff_259_8_value
        
    @ifir_coeff_259_8.setter
    def ifir_coeff_259_8(self,value):
        self.ifir_coeff_259_8_value = value 
        regvalue = self.ifir_coeff_259_8
        # perform operation with reg value 
             
class IFIR_COEFF_25_LSB :
    
    def __init__(self) -> None:
        self.address = 0x65
        self.page = 1
        
    @property
    def ifir_coeff_257_0(self):
        self.ifir_coeff_257_0_pos   = 0
        self.ifir_coeff_257_0_len   = 8
        return self.ifir_coeff_257_0_value
        
    @ifir_coeff_257_0.setter
    def ifir_coeff_257_0(self,value):
        self.ifir_coeff_257_0_value = value 
        regvalue = self.ifir_coeff_257_0
        # perform operation with reg value 
             
class IFIR_COEFF_26_MSB :
    
    def __init__(self) -> None:
        self.address = 0x66
        self.page = 1
        
    @property
    def ifir_coeff_269_8(self):
        self.ifir_coeff_269_8_pos   = 0
        self.ifir_coeff_269_8_len   = 2
        return self.ifir_coeff_269_8_value
        
    @ifir_coeff_269_8.setter
    def ifir_coeff_269_8(self,value):
        self.ifir_coeff_269_8_value = value 
        regvalue = self.ifir_coeff_269_8
        # perform operation with reg value 
             
class IFIR_COEFF_26_LSB :
    
    def __init__(self) -> None:
        self.address = 0x67
        self.page = 1
        
    @property
    def ifir_coeff_267_0(self):
        self.ifir_coeff_267_0_pos   = 0
        self.ifir_coeff_267_0_len   = 8
        return self.ifir_coeff_267_0_value
        
    @ifir_coeff_267_0.setter
    def ifir_coeff_267_0(self,value):
        self.ifir_coeff_267_0_value = value 
        regvalue = self.ifir_coeff_267_0
        # perform operation with reg value 
             
class IFIR_COEFF_27_MSB :
    
    def __init__(self) -> None:
        self.address = 0x68
        self.page = 1
        
    @property
    def ifir_coeff_279_8(self):
        self.ifir_coeff_279_8_pos   = 0
        self.ifir_coeff_279_8_len   = 2
        return self.ifir_coeff_279_8_value
        
    @ifir_coeff_279_8.setter
    def ifir_coeff_279_8(self,value):
        self.ifir_coeff_279_8_value = value 
        regvalue = self.ifir_coeff_279_8
        # perform operation with reg value 
             
class IFIR_COEFF_27_LSB :
    
    def __init__(self) -> None:
        self.address = 0x69
        self.page = 1
        
    @property
    def ifir_coeff_277_0(self):
        self.ifir_coeff_277_0_pos   = 0
        self.ifir_coeff_277_0_len   = 8
        return self.ifir_coeff_277_0_value
        
    @ifir_coeff_277_0.setter
    def ifir_coeff_277_0(self,value):
        self.ifir_coeff_277_0_value = value 
        regvalue = self.ifir_coeff_277_0
        # perform operation with reg value 
             
class IFIR_COEFF_28_MSB :
    
    def __init__(self) -> None:
        self.address = 0x6a
        self.page = 1
        
    @property
    def ifir_coeff_289_8(self):
        self.ifir_coeff_289_8_pos   = 0
        self.ifir_coeff_289_8_len   = 2
        return self.ifir_coeff_289_8_value
        
    @ifir_coeff_289_8.setter
    def ifir_coeff_289_8(self,value):
        self.ifir_coeff_289_8_value = value 
        regvalue = self.ifir_coeff_289_8
        # perform operation with reg value 
             
class IFIR_COEFF_28_LSB :
    
    def __init__(self) -> None:
        self.address = 0x6b
        self.page = 1
        
    @property
    def ifir_coeff_287_0(self):
        self.ifir_coeff_287_0_pos   = 0
        self.ifir_coeff_287_0_len   = 8
        return self.ifir_coeff_287_0_value
        
    @ifir_coeff_287_0.setter
    def ifir_coeff_287_0(self,value):
        self.ifir_coeff_287_0_value = value 
        regvalue = self.ifir_coeff_287_0
        # perform operation with reg value 
             
class IFIR_COEFF_29_MSB :
    
    def __init__(self) -> None:
        self.address = 0x6c
        self.page = 1
        
    @property
    def ifir_coeff_299_8(self):
        self.ifir_coeff_299_8_pos   = 0
        self.ifir_coeff_299_8_len   = 2
        return self.ifir_coeff_299_8_value
        
    @ifir_coeff_299_8.setter
    def ifir_coeff_299_8(self,value):
        self.ifir_coeff_299_8_value = value 
        regvalue = self.ifir_coeff_299_8
        # perform operation with reg value 
             
class IFIR_COEFF_29_LSB :
    
    def __init__(self) -> None:
        self.address = 0x6d
        self.page = 1
        
    @property
    def ifir_coeff_297_0(self):
        self.ifir_coeff_297_0_pos   = 0
        self.ifir_coeff_297_0_len   = 8
        return self.ifir_coeff_297_0_value
        
    @ifir_coeff_297_0.setter
    def ifir_coeff_297_0(self,value):
        self.ifir_coeff_297_0_value = value 
        regvalue = self.ifir_coeff_297_0
        # perform operation with reg value 
             
class IFIR_COEFF_30_MSB :
    
    def __init__(self) -> None:
        self.address = 0x6e
        self.page = 1
        
    @property
    def ifir_coeff_309_8(self):
        self.ifir_coeff_309_8_pos   = 0
        self.ifir_coeff_309_8_len   = 2
        return self.ifir_coeff_309_8_value
        
    @ifir_coeff_309_8.setter
    def ifir_coeff_309_8(self,value):
        self.ifir_coeff_309_8_value = value 
        regvalue = self.ifir_coeff_309_8
        # perform operation with reg value 
             
class IFIR_COEFF_30_LSB :
    
    def __init__(self) -> None:
        self.address = 0x6f
        self.page = 1
        
    @property
    def ifir_coeff_307_0(self):
        self.ifir_coeff_307_0_pos   = 0
        self.ifir_coeff_307_0_len   = 8
        return self.ifir_coeff_307_0_value
        
    @ifir_coeff_307_0.setter
    def ifir_coeff_307_0(self,value):
        self.ifir_coeff_307_0_value = value 
        regvalue = self.ifir_coeff_307_0
        # perform operation with reg value 
             
class IFIR_COEFF_31_MSB :
    
    def __init__(self) -> None:
        self.address = 0x70
        self.page = 1
        
    @property
    def ifir_coeff_319_8(self):
        self.ifir_coeff_319_8_pos   = 0
        self.ifir_coeff_319_8_len   = 2
        return self.ifir_coeff_319_8_value
        
    @ifir_coeff_319_8.setter
    def ifir_coeff_319_8(self,value):
        self.ifir_coeff_319_8_value = value 
        regvalue = self.ifir_coeff_319_8
        # perform operation with reg value 
             
class IFIR_COEFF_31_LSB :
    
    def __init__(self) -> None:
        self.address = 0x71
        self.page = 1
        
    @property
    def ifir_coeff_317_0(self):
        self.ifir_coeff_317_0_pos   = 0
        self.ifir_coeff_317_0_len   = 8
        return self.ifir_coeff_317_0_value
        
    @ifir_coeff_317_0.setter
    def ifir_coeff_317_0(self,value):
        self.ifir_coeff_317_0_value = value 
        regvalue = self.ifir_coeff_317_0
        # perform operation with reg value 
             
class IFIR_COEFF_32_MSB :
    
    def __init__(self) -> None:
        self.address = 0x72
        self.page = 1
        
    @property
    def ifir_coeff_329_8(self):
        self.ifir_coeff_329_8_pos   = 0
        self.ifir_coeff_329_8_len   = 2
        return self.ifir_coeff_329_8_value
        
    @ifir_coeff_329_8.setter
    def ifir_coeff_329_8(self,value):
        self.ifir_coeff_329_8_value = value 
        regvalue = self.ifir_coeff_329_8
        # perform operation with reg value 
             
class IFIR_COEFF_32_LSB :
    
    def __init__(self) -> None:
        self.address = 0x73
        self.page = 1
        
    @property
    def ifir_coeff_327_0(self):
        self.ifir_coeff_327_0_pos   = 0
        self.ifir_coeff_327_0_len   = 8
        return self.ifir_coeff_327_0_value
        
    @ifir_coeff_327_0.setter
    def ifir_coeff_327_0(self,value):
        self.ifir_coeff_327_0_value = value 
        regvalue = self.ifir_coeff_327_0
        # perform operation with reg value 
             
class IFIR_COEFF_33_MSB :
    
    def __init__(self) -> None:
        self.address = 0x74
        self.page = 1
        
    @property
    def ifir_coeff_339_8(self):
        self.ifir_coeff_339_8_pos   = 0
        self.ifir_coeff_339_8_len   = 2
        return self.ifir_coeff_339_8_value
        
    @ifir_coeff_339_8.setter
    def ifir_coeff_339_8(self,value):
        self.ifir_coeff_339_8_value = value 
        regvalue = self.ifir_coeff_339_8
        # perform operation with reg value 
             
class IFIR_COEFF_33_LSB :
    
    def __init__(self) -> None:
        self.address = 0x75
        self.page = 1
        
    @property
    def ifir_coeff_337_0(self):
        self.ifir_coeff_337_0_pos   = 0
        self.ifir_coeff_337_0_len   = 8
        return self.ifir_coeff_337_0_value
        
    @ifir_coeff_337_0.setter
    def ifir_coeff_337_0(self,value):
        self.ifir_coeff_337_0_value = value 
        regvalue = self.ifir_coeff_337_0
        # perform operation with reg value 
             
class IFIR_COEFF_34_MSB :
    
    def __init__(self) -> None:
        self.address = 0x76
        self.page = 1
        
    @property
    def ifir_coeff_349_8(self):
        self.ifir_coeff_349_8_pos   = 0
        self.ifir_coeff_349_8_len   = 2
        return self.ifir_coeff_349_8_value
        
    @ifir_coeff_349_8.setter
    def ifir_coeff_349_8(self,value):
        self.ifir_coeff_349_8_value = value 
        regvalue = self.ifir_coeff_349_8
        # perform operation with reg value 
             
class IFIR_COEFF_34_LSB :
    
    def __init__(self) -> None:
        self.address = 0x77
        self.page = 1
        
    @property
    def ifir_coeff_347_0(self):
        self.ifir_coeff_347_0_pos   = 0
        self.ifir_coeff_347_0_len   = 8
        return self.ifir_coeff_347_0_value
        
    @ifir_coeff_347_0.setter
    def ifir_coeff_347_0(self,value):
        self.ifir_coeff_347_0_value = value 
        regvalue = self.ifir_coeff_347_0
        # perform operation with reg value 
             
class IFIR_COEFF_35_MSB :
    
    def __init__(self) -> None:
        self.address = 0x78
        self.page = 1
        
    @property
    def ifir_coeff_359_8(self):
        self.ifir_coeff_359_8_pos   = 0
        self.ifir_coeff_359_8_len   = 2
        return self.ifir_coeff_359_8_value
        
    @ifir_coeff_359_8.setter
    def ifir_coeff_359_8(self,value):
        self.ifir_coeff_359_8_value = value 
        regvalue = self.ifir_coeff_359_8
        # perform operation with reg value 
             
class IFIR_COEFF_35_LSB :
    
    def __init__(self) -> None:
        self.address = 0x79
        self.page = 1
        
    @property
    def ifir_coeff_357_0(self):
        self.ifir_coeff_357_0_pos   = 0
        self.ifir_coeff_357_0_len   = 8
        return self.ifir_coeff_357_0_value
        
    @ifir_coeff_357_0.setter
    def ifir_coeff_357_0(self,value):
        self.ifir_coeff_357_0_value = value 
        regvalue = self.ifir_coeff_357_0
        # perform operation with reg value 
             
class IFIR_COEFF_36_MSB :
    
    def __init__(self) -> None:
        self.address = 0x7a
        self.page = 1
        
    @property
    def ifir_coeff_369_8(self):
        self.ifir_coeff_369_8_pos   = 0
        self.ifir_coeff_369_8_len   = 2
        return self.ifir_coeff_369_8_value
        
    @ifir_coeff_369_8.setter
    def ifir_coeff_369_8(self,value):
        self.ifir_coeff_369_8_value = value 
        regvalue = self.ifir_coeff_369_8
        # perform operation with reg value 
             
class IFIR_COEFF_36_LSB :
    
    def __init__(self) -> None:
        self.address = 0x7b
        self.page = 1
        
    @property
    def ifir_coeff_367_0(self):
        self.ifir_coeff_367_0_pos   = 0
        self.ifir_coeff_367_0_len   = 8
        return self.ifir_coeff_367_0_value
        
    @ifir_coeff_367_0.setter
    def ifir_coeff_367_0(self,value):
        self.ifir_coeff_367_0_value = value 
        regvalue = self.ifir_coeff_367_0
        # perform operation with reg value 
             
class IFIR_COEFF_37_MSB :
    
    def __init__(self) -> None:
        self.address = 0x7c
        self.page = 1
        
    @property
    def ifir_coeff_379_8(self):
        self.ifir_coeff_379_8_pos   = 0
        self.ifir_coeff_379_8_len   = 2
        return self.ifir_coeff_379_8_value
        
    @ifir_coeff_379_8.setter
    def ifir_coeff_379_8(self,value):
        self.ifir_coeff_379_8_value = value 
        regvalue = self.ifir_coeff_379_8
        # perform operation with reg value 
             
class IFIR_COEFF_37_LSB :
    
    def __init__(self) -> None:
        self.address = 0x7d
        self.page = 1
        
    @property
    def ifir_coeff_377_0(self):
        self.ifir_coeff_377_0_pos   = 0
        self.ifir_coeff_377_0_len   = 8
        return self.ifir_coeff_377_0_value
        
    @ifir_coeff_377_0.setter
    def ifir_coeff_377_0(self,value):
        self.ifir_coeff_377_0_value = value 
        regvalue = self.ifir_coeff_377_0
        # perform operation with reg value 
             
class IFIR_COEFF_38_MSB :
    
    def __init__(self) -> None:
        self.address = 0x7e
        self.page = 1
        
    @property
    def ifir_coeff_389_8(self):
        self.ifir_coeff_389_8_pos   = 0
        self.ifir_coeff_389_8_len   = 2
        return self.ifir_coeff_389_8_value
        
    @ifir_coeff_389_8.setter
    def ifir_coeff_389_8(self,value):
        self.ifir_coeff_389_8_value = value 
        regvalue = self.ifir_coeff_389_8
        # perform operation with reg value 
             
class IFIR_COEFF_38_LSB :
    
    def __init__(self) -> None:
        self.address = 0x7f
        self.page = 1
        
    @property
    def ifir_coeff_387_0(self):
        self.ifir_coeff_387_0_pos   = 0
        self.ifir_coeff_387_0_len   = 8
        return self.ifir_coeff_387_0_value
        
    @ifir_coeff_387_0.setter
    def ifir_coeff_387_0(self,value):
        self.ifir_coeff_387_0_value = value 
        regvalue = self.ifir_coeff_387_0
        # perform operation with reg value 
             
class IFIR_COEFF_39_MSB :
    
    def __init__(self) -> None:
        self.address = 0x80
        self.page = 1
        
    @property
    def ifir_coeff_399_8(self):
        self.ifir_coeff_399_8_pos   = 0
        self.ifir_coeff_399_8_len   = 2
        return self.ifir_coeff_399_8_value
        
    @ifir_coeff_399_8.setter
    def ifir_coeff_399_8(self,value):
        self.ifir_coeff_399_8_value = value 
        regvalue = self.ifir_coeff_399_8
        # perform operation with reg value 
             
class IFIR_COEFF_39_LSB :
    
    def __init__(self) -> None:
        self.address = 0x81
        self.page = 1
        
    @property
    def ifir_coeff_397_0(self):
        self.ifir_coeff_397_0_pos   = 0
        self.ifir_coeff_397_0_len   = 8
        return self.ifir_coeff_397_0_value
        
    @ifir_coeff_397_0.setter
    def ifir_coeff_397_0(self,value):
        self.ifir_coeff_397_0_value = value 
        regvalue = self.ifir_coeff_397_0
        # perform operation with reg value 
             
class IFIR_Spare_Register :
    
    def __init__(self) -> None:
        self.address = 0x8f
        self.page = 1
        
    @property
    def ifir_spare7_0(self):
        self.ifir_spare7_0_pos   = 0
        self.ifir_spare7_0_len   = 8
        return self.ifir_spare7_0_value
        
    @ifir_spare7_0.setter
    def ifir_spare7_0(self,value):
        self.ifir_spare7_0_value = value 
        regvalue = self.ifir_spare7_0
        # perform operation with reg value 
             
class OTP_control_reg_1 :
    
    def __init__(self) -> None:
        self.address = 0xae
        self.page = 1
        
    @property
    def otp_status(self):
        self.otp_status_pos   = 7
        self.otp_status_len   = 1
        return self.otp_status_value
        
    @otp_status.setter
    def otp_status(self,value):
        self.otp_status_value = value 
        regvalue = self.otp_status
        # perform operation with reg value 
            
    @property
    def otp_result(self):
        self.otp_result_pos   = 6
        self.otp_result_len   = 1
        return self.otp_result_value
        
    @otp_result.setter
    def otp_result(self,value):
        self.otp_result_value = value 
        regvalue = self.otp_result
        # perform operation with reg value 
            
    @property
    def otp_margin_read(self):
        self.otp_margin_read_pos   = 2
        self.otp_margin_read_len   = 1
        return self.otp_margin_read_value
        
    @otp_margin_read.setter
    def otp_margin_read(self,value):
        self.otp_margin_read_value = value 
        regvalue = self.otp_margin_read
        # perform operation with reg value 
            
    @property
    def otp_burn(self):
        self.otp_burn_pos   = 1
        self.otp_burn_len   = 1
        return self.otp_burn_value
        
    @otp_burn.setter
    def otp_burn(self,value):
        self.otp_burn_value = value 
        regvalue = self.otp_burn
        # perform operation with reg value 
            
    @property
    def otp_load(self):
        self.otp_load_pos   = 0
        self.otp_load_len   = 1
        return self.otp_load_value
        
    @otp_load.setter
    def otp_load(self,value):
        self.otp_load_value = value 
        regvalue = self.otp_load
        # perform operation with reg value 
             
class OTP_control_reg_2 :
    
    def __init__(self) -> None:
        self.address = 0xaf
        self.page = 1
        
    @property
    def otp_single_byte(self):
        self.otp_single_byte_pos   = 7
        self.otp_single_byte_len   = 1
        return self.otp_single_byte_value
        
    @otp_single_byte.setter
    def otp_single_byte(self,value):
        self.otp_single_byte_value = value 
        regvalue = self.otp_single_byte
        # perform operation with reg value 
            
    @property
    def otp_margin_read_mode(self):
        self.otp_margin_read_mode_pos   = 6
        self.otp_margin_read_mode_len   = 1
        return self.otp_margin_read_mode_value
        
    @otp_margin_read_mode.setter
    def otp_margin_read_mode(self,value):
        self.otp_margin_read_mode_value = value 
        regvalue = self.otp_margin_read_mode
        # perform operation with reg value 
            
    @property
    def otp_addr5_0(self):
        self.otp_addr5_0_pos   = 0
        self.otp_addr5_0_len   = 6
        return self.otp_addr5_0_value
        
    @otp_addr5_0.setter
    def otp_addr5_0(self,value):
        self.otp_addr5_0_value = value 
        regvalue = self.otp_addr5_0
        # perform operation with reg value 
             
class OTP_FIELDS_0 :
    
    def __init__(self) -> None:
        self.address = 0xb0
        self.page = 1
        
    @property
    def vbgr_adj3_0(self):
        self.vbgr_adj3_0_pos   = 4
        self.vbgr_adj3_0_len   = 4
        return self.vbgr_adj3_0_value
        
    @vbgr_adj3_0.setter
    def vbgr_adj3_0(self,value):
        self.vbgr_adj3_0_value = value 
        regvalue = self.vbgr_adj3_0
        # perform operation with reg value 
            
    @property
    def i3c_instance_id(self):
        self.i3c_instance_id_pos   = 3
        self.i3c_instance_id_len   = 1
        return self.i3c_instance_id_value
        
    @i3c_instance_id.setter
    def i3c_instance_id(self,value):
        self.i3c_instance_id_value = value 
        regvalue = self.i3c_instance_id
        # perform operation with reg value 
            
    @property
    def i2c_slave_id(self):
        self.i2c_slave_id_pos   = 2
        self.i2c_slave_id_len   = 1
        return self.i2c_slave_id_value
        
    @i2c_slave_id.setter
    def i2c_slave_id(self,value):
        self.i2c_slave_id_value = value 
        regvalue = self.i2c_slave_id
        # perform operation with reg value 
            
    @property
    def i3c_dis(self):
        self.i3c_dis_pos   = 1
        self.i3c_dis_len   = 1
        return self.i3c_dis_value
        
    @i3c_dis.setter
    def i3c_dis(self,value):
        self.i3c_dis_value = value 
        regvalue = self.i3c_dis
        # perform operation with reg value 
            
    @property
    def otp_burnt_b(self):
        self.otp_burnt_b_pos   = 0
        self.otp_burnt_b_len   = 1
        return self.otp_burnt_b_value
        
    @otp_burnt_b.setter
    def otp_burnt_b(self,value):
        self.otp_burnt_b_value = value 
        regvalue = self.otp_burnt_b
        # perform operation with reg value 
             
class OTP_FIELDS_1 :
    
    def __init__(self) -> None:
        self.address = 0xb1
        self.page = 1
        
    @property
    def otp_vbg_curv_adj3_0(self):
        self.otp_vbg_curv_adj3_0_pos   = 4
        self.otp_vbg_curv_adj3_0_len   = 4
        return self.otp_vbg_curv_adj3_0_value
        
    @otp_vbg_curv_adj3_0.setter
    def otp_vbg_curv_adj3_0(self,value):
        self.otp_vbg_curv_adj3_0_value = value 
        regvalue = self.otp_vbg_curv_adj3_0
        # perform operation with reg value 
            
    @property
    def bst_ocp_trim3_0(self):
        self.bst_ocp_trim3_0_pos   = 0
        self.bst_ocp_trim3_0_len   = 4
        return self.bst_ocp_trim3_0_value
        
    @bst_ocp_trim3_0.setter
    def bst_ocp_trim3_0(self,value):
        self.bst_ocp_trim3_0_value = value 
        regvalue = self.bst_ocp_trim3_0
        # perform operation with reg value 
             
class OTP_FIELDS_2 :
    
    def __init__(self) -> None:
        self.address = 0xb2
        self.page = 1
        
    @property
    def platf_pdm_freq_p01_0(self):
        self.platf_pdm_freq_p01_0_pos   = 6
        self.platf_pdm_freq_p01_0_len   = 2
        return self.platf_pdm_freq_p01_0_value
        
    @platf_pdm_freq_p01_0.setter
    def platf_pdm_freq_p01_0(self,value):
        self.platf_pdm_freq_p01_0_value = value 
        regvalue = self.platf_pdm_freq_p01_0
        # perform operation with reg value 
            
    @property
    def bst_ocp_trim4(self):
        self.bst_ocp_trim4_pos   = 5
        self.bst_ocp_trim4_len   = 1
        return self.bst_ocp_trim4_value
        
    @bst_ocp_trim4.setter
    def bst_ocp_trim4(self,value):
        self.bst_ocp_trim4_value = value 
        regvalue = self.bst_ocp_trim4
        # perform operation with reg value 
            
    @property
    def bst_zc_trim4_0(self):
        self.bst_zc_trim4_0_pos   = 0
        self.bst_zc_trim4_0_len   = 5
        return self.bst_zc_trim4_0_value
        
    @bst_zc_trim4_0.setter
    def bst_zc_trim4_0(self,value):
        self.bst_zc_trim4_0_value = value 
        regvalue = self.bst_zc_trim4_0
        # perform operation with reg value 
             
class OTP_FIELDS_3 :
    
    def __init__(self) -> None:
        self.address = 0xb3
        self.page = 1
        
    @property
    def tsd_pvt_adj2_0(self):
        self.tsd_pvt_adj2_0_pos   = 5
        self.tsd_pvt_adj2_0_len   = 3
        return self.tsd_pvt_adj2_0_value
        
    @tsd_pvt_adj2_0.setter
    def tsd_pvt_adj2_0(self,value):
        self.tsd_pvt_adj2_0_value = value 
        regvalue = self.tsd_pvt_adj2_0
        # perform operation with reg value 
            
    @property
    def spare13(self):
        self.spare13_pos   = 4
        self.spare13_len   = 1
        return self.spare13_value
        
    @spare13.setter
    def spare13(self,value):
        self.spare13_value = value 
        regvalue = self.spare13
        # perform operation with reg value 
            
    @property
    def spare23_0(self):
        self.spare23_0_pos   = 0
        self.spare23_0_len   = 4
        return self.spare23_0_value
        
    @spare23_0.setter
    def spare23_0(self,value):
        self.spare23_0_value = value 
        regvalue = self.spare23_0
        # perform operation with reg value 
             
class OTP_FIELDS_4 :
    
    def __init__(self) -> None:
        self.address = 0xb4
        self.page = 1
        
    @property
    def platf_input_mode_p01_0(self):
        self.platf_input_mode_p01_0_pos   = 6
        self.platf_input_mode_p01_0_len   = 2
        return self.platf_input_mode_p01_0_value
        
    @platf_input_mode_p01_0.setter
    def platf_input_mode_p01_0(self,value):
        self.platf_input_mode_p01_0_value = value 
        regvalue = self.platf_input_mode_p01_0
        # perform operation with reg value 
            
    @property
    def otp_bst_comp_bso_trim5_0(self):
        self.otp_bst_comp_bso_trim5_0_pos   = 0
        self.otp_bst_comp_bso_trim5_0_len   = 6
        return self.otp_bst_comp_bso_trim5_0_value
        
    @otp_bst_comp_bso_trim5_0.setter
    def otp_bst_comp_bso_trim5_0(self,value):
        self.otp_bst_comp_bso_trim5_0_value = value 
        regvalue = self.otp_bst_comp_bso_trim5_0
        # perform operation with reg value 
             
class OTP_FIELDS_5 :
    
    def __init__(self) -> None:
        self.address = 0xb5
        self.page = 1
        
    @property
    def platf_input_mode_p11_0(self):
        self.platf_input_mode_p11_0_pos   = 6
        self.platf_input_mode_p11_0_len   = 2
        return self.platf_input_mode_p11_0_value
        
    @platf_input_mode_p11_0.setter
    def platf_input_mode_p11_0(self,value):
        self.platf_input_mode_p11_0_value = value 
        regvalue = self.platf_input_mode_p11_0
        # perform operation with reg value 
            
    @property
    def otp_bst_comp_bias_trim5_0(self):
        self.otp_bst_comp_bias_trim5_0_pos   = 0
        self.otp_bst_comp_bias_trim5_0_len   = 6
        return self.otp_bst_comp_bias_trim5_0_value
        
    @otp_bst_comp_bias_trim5_0.setter
    def otp_bst_comp_bias_trim5_0(self,value):
        self.otp_bst_comp_bias_trim5_0_value = value 
        regvalue = self.otp_bst_comp_bias_trim5_0
        # perform operation with reg value 
             
class OTP_FIELDS_6 :
    
    def __init__(self) -> None:
        self.address = 0xb6
        self.page = 1
        
    @property
    def platf_input_mode_p21_0(self):
        self.platf_input_mode_p21_0_pos   = 6
        self.platf_input_mode_p21_0_len   = 2
        return self.platf_input_mode_p21_0_value
        
    @platf_input_mode_p21_0.setter
    def platf_input_mode_p21_0(self,value):
        self.platf_input_mode_p21_0_value = value 
        regvalue = self.platf_input_mode_p21_0
        # perform operation with reg value 
            
    @property
    def platf_tdm_fsyn_rate_p02_0(self):
        self.platf_tdm_fsyn_rate_p02_0_pos   = 3
        self.platf_tdm_fsyn_rate_p02_0_len   = 3
        return self.platf_tdm_fsyn_rate_p02_0_value
        
    @platf_tdm_fsyn_rate_p02_0.setter
    def platf_tdm_fsyn_rate_p02_0(self,value):
        self.platf_tdm_fsyn_rate_p02_0_value = value 
        regvalue = self.platf_tdm_fsyn_rate_p02_0
        # perform operation with reg value 
            
    @property
    def platf_tdm_bclk_osr_p02_0(self):
        self.platf_tdm_bclk_osr_p02_0_pos   = 0
        self.platf_tdm_bclk_osr_p02_0_len   = 3
        return self.platf_tdm_bclk_osr_p02_0_value
        
    @platf_tdm_bclk_osr_p02_0.setter
    def platf_tdm_bclk_osr_p02_0(self,value):
        self.platf_tdm_bclk_osr_p02_0_value = value 
        regvalue = self.platf_tdm_bclk_osr_p02_0
        # perform operation with reg value 
             
class OTP_FIELDS_7 :
    
    def __init__(self) -> None:
        self.address = 0xb7
        self.page = 1
        
    @property
    def platf_input_mode_p31_0(self):
        self.platf_input_mode_p31_0_pos   = 6
        self.platf_input_mode_p31_0_len   = 2
        return self.platf_input_mode_p31_0_value
        
    @platf_input_mode_p31_0.setter
    def platf_input_mode_p31_0(self,value):
        self.platf_input_mode_p31_0_value = value 
        regvalue = self.platf_input_mode_p31_0
        # perform operation with reg value 
            
    @property
    def platf_tdm_fsyn_rate_p12_0(self):
        self.platf_tdm_fsyn_rate_p12_0_pos   = 3
        self.platf_tdm_fsyn_rate_p12_0_len   = 3
        return self.platf_tdm_fsyn_rate_p12_0_value
        
    @platf_tdm_fsyn_rate_p12_0.setter
    def platf_tdm_fsyn_rate_p12_0(self,value):
        self.platf_tdm_fsyn_rate_p12_0_value = value 
        regvalue = self.platf_tdm_fsyn_rate_p12_0
        # perform operation with reg value 
            
    @property
    def platf_tdm_bclk_osr_p12_0(self):
        self.platf_tdm_bclk_osr_p12_0_pos   = 0
        self.platf_tdm_bclk_osr_p12_0_len   = 3
        return self.platf_tdm_bclk_osr_p12_0_value
        
    @platf_tdm_bclk_osr_p12_0.setter
    def platf_tdm_bclk_osr_p12_0(self,value):
        self.platf_tdm_bclk_osr_p12_0_value = value 
        regvalue = self.platf_tdm_bclk_osr_p12_0
        # perform operation with reg value 
             
class OTP_FIELDS_8 :
    
    def __init__(self) -> None:
        self.address = 0xb8
        self.page = 1
        
    @property
    def bst_loop_res_force(self):
        self.bst_loop_res_force_pos   = 7
        self.bst_loop_res_force_len   = 1
        return self.bst_loop_res_force_value
        
    @bst_loop_res_force.setter
    def bst_loop_res_force(self,value):
        self.bst_loop_res_force_value = value 
        regvalue = self.bst_loop_res_force
        # perform operation with reg value 
            
    @property
    def platf_dpa_ana_gain_p02_0(self):
        self.platf_dpa_ana_gain_p02_0_pos   = 4
        self.platf_dpa_ana_gain_p02_0_len   = 3
        return self.platf_dpa_ana_gain_p02_0_value
        
    @platf_dpa_ana_gain_p02_0.setter
    def platf_dpa_ana_gain_p02_0(self,value):
        self.platf_dpa_ana_gain_p02_0_value = value 
        regvalue = self.platf_dpa_ana_gain_p02_0
        # perform operation with reg value 
            
    @property
    def platf_pdm_mode_low_freq(self):
        self.platf_pdm_mode_low_freq_pos   = 3
        self.platf_pdm_mode_low_freq_len   = 1
        return self.platf_pdm_mode_low_freq_value
        
    @platf_pdm_mode_low_freq.setter
    def platf_pdm_mode_low_freq(self,value):
        self.platf_pdm_mode_low_freq_value = value 
        regvalue = self.platf_pdm_mode_low_freq
        # perform operation with reg value 
            
    @property
    def platf_dpa_ana_gain_p12_0(self):
        self.platf_dpa_ana_gain_p12_0_pos   = 0
        self.platf_dpa_ana_gain_p12_0_len   = 3
        return self.platf_dpa_ana_gain_p12_0_value
        
    @platf_dpa_ana_gain_p12_0.setter
    def platf_dpa_ana_gain_p12_0(self,value):
        self.platf_dpa_ana_gain_p12_0_value = value 
        regvalue = self.platf_dpa_ana_gain_p12_0
        # perform operation with reg value 
             
class OTP_FIELDS_9 :
    
    def __init__(self) -> None:
        self.address = 0xb9
        self.page = 1
        
    @property
    def i3c_remapping_page_sel_3(self):
        self.i3c_remapping_page_sel_3_pos   = 7
        self.i3c_remapping_page_sel_3_len   = 1
        return self.i3c_remapping_page_sel_3_value
        
    @i3c_remapping_page_sel_3.setter
    def i3c_remapping_page_sel_3(self,value):
        self.i3c_remapping_page_sel_3_value = value 
        regvalue = self.i3c_remapping_page_sel_3
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_3(self):
        self.i3c_remapping_en_3_pos   = 6
        self.i3c_remapping_en_3_len   = 1
        return self.i3c_remapping_en_3_value
        
    @i3c_remapping_en_3.setter
    def i3c_remapping_en_3(self,value):
        self.i3c_remapping_en_3_value = value 
        regvalue = self.i3c_remapping_en_3
        # perform operation with reg value 
            
    @property
    def i3c_remapping_page_sel_2(self):
        self.i3c_remapping_page_sel_2_pos   = 5
        self.i3c_remapping_page_sel_2_len   = 1
        return self.i3c_remapping_page_sel_2_value
        
    @i3c_remapping_page_sel_2.setter
    def i3c_remapping_page_sel_2(self,value):
        self.i3c_remapping_page_sel_2_value = value 
        regvalue = self.i3c_remapping_page_sel_2
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_2(self):
        self.i3c_remapping_en_2_pos   = 4
        self.i3c_remapping_en_2_len   = 1
        return self.i3c_remapping_en_2_value
        
    @i3c_remapping_en_2.setter
    def i3c_remapping_en_2(self,value):
        self.i3c_remapping_en_2_value = value 
        regvalue = self.i3c_remapping_en_2
        # perform operation with reg value 
            
    @property
    def i3c_remapping_page_sel_1(self):
        self.i3c_remapping_page_sel_1_pos   = 3
        self.i3c_remapping_page_sel_1_len   = 1
        return self.i3c_remapping_page_sel_1_value
        
    @i3c_remapping_page_sel_1.setter
    def i3c_remapping_page_sel_1(self,value):
        self.i3c_remapping_page_sel_1_value = value 
        regvalue = self.i3c_remapping_page_sel_1
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_1(self):
        self.i3c_remapping_en_1_pos   = 2
        self.i3c_remapping_en_1_len   = 1
        return self.i3c_remapping_en_1_value
        
    @i3c_remapping_en_1.setter
    def i3c_remapping_en_1(self,value):
        self.i3c_remapping_en_1_value = value 
        regvalue = self.i3c_remapping_en_1
        # perform operation with reg value 
            
    @property
    def i3c_remapping_page_sel_0(self):
        self.i3c_remapping_page_sel_0_pos   = 1
        self.i3c_remapping_page_sel_0_len   = 1
        return self.i3c_remapping_page_sel_0_value
        
    @i3c_remapping_page_sel_0.setter
    def i3c_remapping_page_sel_0(self,value):
        self.i3c_remapping_page_sel_0_value = value 
        regvalue = self.i3c_remapping_page_sel_0
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_0(self):
        self.i3c_remapping_en_0_pos   = 0
        self.i3c_remapping_en_0_len   = 1
        return self.i3c_remapping_en_0_value
        
    @i3c_remapping_en_0.setter
    def i3c_remapping_en_0(self,value):
        self.i3c_remapping_en_0_value = value 
        regvalue = self.i3c_remapping_en_0
        # perform operation with reg value 
             
class OTP_FIELDS_10 :
    
    def __init__(self) -> None:
        self.address = 0xba
        self.page = 1
        
    @property
    def platf_pdm_freq_p11_0(self):
        self.platf_pdm_freq_p11_0_pos   = 6
        self.platf_pdm_freq_p11_0_len   = 2
        return self.platf_pdm_freq_p11_0_value
        
    @platf_pdm_freq_p11_0.setter
    def platf_pdm_freq_p11_0(self,value):
        self.platf_pdm_freq_p11_0_value = value 
        regvalue = self.platf_pdm_freq_p11_0
        # perform operation with reg value 
            
    @property
    def i3c_remapping_page_sel_6(self):
        self.i3c_remapping_page_sel_6_pos   = 5
        self.i3c_remapping_page_sel_6_len   = 1
        return self.i3c_remapping_page_sel_6_value
        
    @i3c_remapping_page_sel_6.setter
    def i3c_remapping_page_sel_6(self,value):
        self.i3c_remapping_page_sel_6_value = value 
        regvalue = self.i3c_remapping_page_sel_6
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_6(self):
        self.i3c_remapping_en_6_pos   = 4
        self.i3c_remapping_en_6_len   = 1
        return self.i3c_remapping_en_6_value
        
    @i3c_remapping_en_6.setter
    def i3c_remapping_en_6(self,value):
        self.i3c_remapping_en_6_value = value 
        regvalue = self.i3c_remapping_en_6
        # perform operation with reg value 
            
    @property
    def i3c_remapping_page_sel_5(self):
        self.i3c_remapping_page_sel_5_pos   = 3
        self.i3c_remapping_page_sel_5_len   = 1
        return self.i3c_remapping_page_sel_5_value
        
    @i3c_remapping_page_sel_5.setter
    def i3c_remapping_page_sel_5(self,value):
        self.i3c_remapping_page_sel_5_value = value 
        regvalue = self.i3c_remapping_page_sel_5
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_5(self):
        self.i3c_remapping_en_5_pos   = 2
        self.i3c_remapping_en_5_len   = 1
        return self.i3c_remapping_en_5_value
        
    @i3c_remapping_en_5.setter
    def i3c_remapping_en_5(self,value):
        self.i3c_remapping_en_5_value = value 
        regvalue = self.i3c_remapping_en_5
        # perform operation with reg value 
            
    @property
    def i3c_remapping_page_sel_4(self):
        self.i3c_remapping_page_sel_4_pos   = 1
        self.i3c_remapping_page_sel_4_len   = 1
        return self.i3c_remapping_page_sel_4_value
        
    @i3c_remapping_page_sel_4.setter
    def i3c_remapping_page_sel_4(self,value):
        self.i3c_remapping_page_sel_4_value = value 
        regvalue = self.i3c_remapping_page_sel_4
        # perform operation with reg value 
            
    @property
    def i3c_remapping_en_4(self):
        self.i3c_remapping_en_4_pos   = 0
        self.i3c_remapping_en_4_len   = 1
        return self.i3c_remapping_en_4_value
        
    @i3c_remapping_en_4.setter
    def i3c_remapping_en_4(self,value):
        self.i3c_remapping_en_4_value = value 
        regvalue = self.i3c_remapping_en_4
        # perform operation with reg value 
             
class OTP_FIELDS_11 :
    
    def __init__(self) -> None:
        self.address = 0xbb
        self.page = 1
        
    @property
    def i3c_remapping_add_07_0(self):
        self.i3c_remapping_add_07_0_pos   = 0
        self.i3c_remapping_add_07_0_len   = 8
        return self.i3c_remapping_add_07_0_value
        
    @i3c_remapping_add_07_0.setter
    def i3c_remapping_add_07_0(self,value):
        self.i3c_remapping_add_07_0_value = value 
        regvalue = self.i3c_remapping_add_07_0
        # perform operation with reg value 
             
class OTP_FIELDS_12 :
    
    def __init__(self) -> None:
        self.address = 0xbc
        self.page = 1
        
    @property
    def i3c_remapping_data_07_0(self):
        self.i3c_remapping_data_07_0_pos   = 0
        self.i3c_remapping_data_07_0_len   = 8
        return self.i3c_remapping_data_07_0_value
        
    @i3c_remapping_data_07_0.setter
    def i3c_remapping_data_07_0(self,value):
        self.i3c_remapping_data_07_0_value = value 
        regvalue = self.i3c_remapping_data_07_0
        # perform operation with reg value 
             
class OTP_FIELDS_13 :
    
    def __init__(self) -> None:
        self.address = 0xbd
        self.page = 1
        
    @property
    def i3c_remapping_add_17_0(self):
        self.i3c_remapping_add_17_0_pos   = 0
        self.i3c_remapping_add_17_0_len   = 8
        return self.i3c_remapping_add_17_0_value
        
    @i3c_remapping_add_17_0.setter
    def i3c_remapping_add_17_0(self,value):
        self.i3c_remapping_add_17_0_value = value 
        regvalue = self.i3c_remapping_add_17_0
        # perform operation with reg value 
             
class OTP_FIELDS_14 :
    
    def __init__(self) -> None:
        self.address = 0xbe
        self.page = 1
        
    @property
    def i3c_remapping_data_17_0(self):
        self.i3c_remapping_data_17_0_pos   = 0
        self.i3c_remapping_data_17_0_len   = 8
        return self.i3c_remapping_data_17_0_value
        
    @i3c_remapping_data_17_0.setter
    def i3c_remapping_data_17_0(self,value):
        self.i3c_remapping_data_17_0_value = value 
        regvalue = self.i3c_remapping_data_17_0
        # perform operation with reg value 
             
class OTP_FIELDS_15 :
    
    def __init__(self) -> None:
        self.address = 0xbf
        self.page = 1
        
    @property
    def i3c_remapping_add_27_0(self):
        self.i3c_remapping_add_27_0_pos   = 0
        self.i3c_remapping_add_27_0_len   = 8
        return self.i3c_remapping_add_27_0_value
        
    @i3c_remapping_add_27_0.setter
    def i3c_remapping_add_27_0(self,value):
        self.i3c_remapping_add_27_0_value = value 
        regvalue = self.i3c_remapping_add_27_0
        # perform operation with reg value 
             
class OTP_FIELDS_16 :
    
    def __init__(self) -> None:
        self.address = 0xc0
        self.page = 1
        
    @property
    def i3c_remapping_data_27_0(self):
        self.i3c_remapping_data_27_0_pos   = 0
        self.i3c_remapping_data_27_0_len   = 8
        return self.i3c_remapping_data_27_0_value
        
    @i3c_remapping_data_27_0.setter
    def i3c_remapping_data_27_0(self,value):
        self.i3c_remapping_data_27_0_value = value 
        regvalue = self.i3c_remapping_data_27_0
        # perform operation with reg value 
             
class OTP_FIELDS_17 :
    
    def __init__(self) -> None:
        self.address = 0xc1
        self.page = 1
        
    @property
    def i3c_remapping_add_37_0(self):
        self.i3c_remapping_add_37_0_pos   = 0
        self.i3c_remapping_add_37_0_len   = 8
        return self.i3c_remapping_add_37_0_value
        
    @i3c_remapping_add_37_0.setter
    def i3c_remapping_add_37_0(self,value):
        self.i3c_remapping_add_37_0_value = value 
        regvalue = self.i3c_remapping_add_37_0
        # perform operation with reg value 
             
class OTP_FIELDS_18 :
    
    def __init__(self) -> None:
        self.address = 0xc2
        self.page = 1
        
    @property
    def i3c_remapping_data_37_0(self):
        self.i3c_remapping_data_37_0_pos   = 0
        self.i3c_remapping_data_37_0_len   = 8
        return self.i3c_remapping_data_37_0_value
        
    @i3c_remapping_data_37_0.setter
    def i3c_remapping_data_37_0(self,value):
        self.i3c_remapping_data_37_0_value = value 
        regvalue = self.i3c_remapping_data_37_0
        # perform operation with reg value 
             
class OTP_FIELDS_19 :
    
    def __init__(self) -> None:
        self.address = 0xc3
        self.page = 1
        
    @property
    def i3c_remapping_add_47_0(self):
        self.i3c_remapping_add_47_0_pos   = 0
        self.i3c_remapping_add_47_0_len   = 8
        return self.i3c_remapping_add_47_0_value
        
    @i3c_remapping_add_47_0.setter
    def i3c_remapping_add_47_0(self,value):
        self.i3c_remapping_add_47_0_value = value 
        regvalue = self.i3c_remapping_add_47_0
        # perform operation with reg value 
             
class OTP_FIELDS_20 :
    
    def __init__(self) -> None:
        self.address = 0xc4
        self.page = 1
        
    @property
    def i3c_remapping_data_47_0(self):
        self.i3c_remapping_data_47_0_pos   = 0
        self.i3c_remapping_data_47_0_len   = 8
        return self.i3c_remapping_data_47_0_value
        
    @i3c_remapping_data_47_0.setter
    def i3c_remapping_data_47_0(self,value):
        self.i3c_remapping_data_47_0_value = value 
        regvalue = self.i3c_remapping_data_47_0
        # perform operation with reg value 
             
class OTP_FIELDS_21 :
    
    def __init__(self) -> None:
        self.address = 0xc5
        self.page = 1
        
    @property
    def i3c_remapping_add_57_0(self):
        self.i3c_remapping_add_57_0_pos   = 0
        self.i3c_remapping_add_57_0_len   = 8
        return self.i3c_remapping_add_57_0_value
        
    @i3c_remapping_add_57_0.setter
    def i3c_remapping_add_57_0(self,value):
        self.i3c_remapping_add_57_0_value = value 
        regvalue = self.i3c_remapping_add_57_0
        # perform operation with reg value 
             
class OTP_FIELDS_22 :
    
    def __init__(self) -> None:
        self.address = 0xc6
        self.page = 1
        
    @property
    def i3c_remapping_data_57_0(self):
        self.i3c_remapping_data_57_0_pos   = 0
        self.i3c_remapping_data_57_0_len   = 8
        return self.i3c_remapping_data_57_0_value
        
    @i3c_remapping_data_57_0.setter
    def i3c_remapping_data_57_0(self,value):
        self.i3c_remapping_data_57_0_value = value 
        regvalue = self.i3c_remapping_data_57_0
        # perform operation with reg value 
             
class OTP_FIELDS_23 :
    
    def __init__(self) -> None:
        self.address = 0xc7
        self.page = 1
        
    @property
    def i3c_remapping_add_67_0(self):
        self.i3c_remapping_add_67_0_pos   = 0
        self.i3c_remapping_add_67_0_len   = 8
        return self.i3c_remapping_add_67_0_value
        
    @i3c_remapping_add_67_0.setter
    def i3c_remapping_add_67_0(self,value):
        self.i3c_remapping_add_67_0_value = value 
        regvalue = self.i3c_remapping_add_67_0
        # perform operation with reg value 
             
class OTP_FIELDS_24 :
    
    def __init__(self) -> None:
        self.address = 0xc8
        self.page = 1
        
    @property
    def i3c_remapping_data_67_0(self):
        self.i3c_remapping_data_67_0_pos   = 0
        self.i3c_remapping_data_67_0_len   = 8
        return self.i3c_remapping_data_67_0_value
        
    @i3c_remapping_data_67_0.setter
    def i3c_remapping_data_67_0(self,value):
        self.i3c_remapping_data_67_0_value = value 
        regvalue = self.i3c_remapping_data_67_0
        # perform operation with reg value 
             
class OTP_FIELDS_25 :
    
    def __init__(self) -> None:
        self.address = 0xc9
        self.page = 1
        
    @property
    def bst_loop_res1(self):
        self.bst_loop_res1_pos   = 7
        self.bst_loop_res1_len   = 1
        return self.bst_loop_res1_value
        
    @bst_loop_res1.setter
    def bst_loop_res1(self,value):
        self.bst_loop_res1_value = value 
        regvalue = self.bst_loop_res1
        # perform operation with reg value 
            
    @property
    def platf_dpa_ana_gain_p22_0(self):
        self.platf_dpa_ana_gain_p22_0_pos   = 4
        self.platf_dpa_ana_gain_p22_0_len   = 3
        return self.platf_dpa_ana_gain_p22_0_value
        
    @platf_dpa_ana_gain_p22_0.setter
    def platf_dpa_ana_gain_p22_0(self,value):
        self.platf_dpa_ana_gain_p22_0_value = value 
        regvalue = self.platf_dpa_ana_gain_p22_0
        # perform operation with reg value 
            
    @property
    def bst_loop_res0(self):
        self.bst_loop_res0_pos   = 3
        self.bst_loop_res0_len   = 1
        return self.bst_loop_res0_value
        
    @bst_loop_res0.setter
    def bst_loop_res0(self,value):
        self.bst_loop_res0_value = value 
        regvalue = self.bst_loop_res0
        # perform operation with reg value 
            
    @property
    def platf_dpa_ana_gain_p32_0(self):
        self.platf_dpa_ana_gain_p32_0_pos   = 0
        self.platf_dpa_ana_gain_p32_0_len   = 3
        return self.platf_dpa_ana_gain_p32_0_value
        
    @platf_dpa_ana_gain_p32_0.setter
    def platf_dpa_ana_gain_p32_0(self,value):
        self.platf_dpa_ana_gain_p32_0_value = value 
        regvalue = self.platf_dpa_ana_gain_p32_0
        # perform operation with reg value 
             
class OTP_FIELDS_26 :
    
    def __init__(self) -> None:
        self.address = 0xca
        self.page = 1
        
    @property
    def int_dig_zero_off11_4(self):
        self.int_dig_zero_off11_4_pos   = 0
        self.int_dig_zero_off11_4_len   = 8
        return self.int_dig_zero_off11_4_value
        
    @int_dig_zero_off11_4.setter
    def int_dig_zero_off11_4(self,value):
        self.int_dig_zero_off11_4_value = value 
        regvalue = self.int_dig_zero_off11_4
        # perform operation with reg value 
             
class OTP_FIELDS_27 :
    
    def __init__(self) -> None:
        self.address = 0xcb
        self.page = 1
        
    @property
    def int_dig_zero_off3_0(self):
        self.int_dig_zero_off3_0_pos   = 4
        self.int_dig_zero_off3_0_len   = 4
        return self.int_dig_zero_off3_0_value
        
    @int_dig_zero_off3_0.setter
    def int_dig_zero_off3_0(self,value):
        self.int_dig_zero_off3_0_value = value 
        regvalue = self.int_dig_zero_off3_0
        # perform operation with reg value 
            
    @property
    def int_dig_idle_off11_8(self):
        self.int_dig_idle_off11_8_pos   = 0
        self.int_dig_idle_off11_8_len   = 4
        return self.int_dig_idle_off11_8_value
        
    @int_dig_idle_off11_8.setter
    def int_dig_idle_off11_8(self,value):
        self.int_dig_idle_off11_8_value = value 
        regvalue = self.int_dig_idle_off11_8
        # perform operation with reg value 
             
class OTP_FIELDS_28 :
    
    def __init__(self) -> None:
        self.address = 0xcc
        self.page = 1
        
    @property
    def int_dig_idle_off7_0(self):
        self.int_dig_idle_off7_0_pos   = 0
        self.int_dig_idle_off7_0_len   = 8
        return self.int_dig_idle_off7_0_value
        
    @int_dig_idle_off7_0.setter
    def int_dig_idle_off7_0(self,value):
        self.int_dig_idle_off7_0_value = value 
        regvalue = self.int_dig_idle_off7_0
        # perform operation with reg value 
             
class OTP_FIELDS_29 :
    
    def __init__(self) -> None:
        self.address = 0xcd
        self.page = 1
        
    @property
    def diff_dig_zero_off11_4(self):
        self.diff_dig_zero_off11_4_pos   = 0
        self.diff_dig_zero_off11_4_len   = 8
        return self.diff_dig_zero_off11_4_value
        
    @diff_dig_zero_off11_4.setter
    def diff_dig_zero_off11_4(self,value):
        self.diff_dig_zero_off11_4_value = value 
        regvalue = self.diff_dig_zero_off11_4
        # perform operation with reg value 
             
class OTP_FIELDS_30 :
    
    def __init__(self) -> None:
        self.address = 0xce
        self.page = 1
        
    @property
    def diff_dig_zero_off3_0(self):
        self.diff_dig_zero_off3_0_pos   = 4
        self.diff_dig_zero_off3_0_len   = 4
        return self.diff_dig_zero_off3_0_value
        
    @diff_dig_zero_off3_0.setter
    def diff_dig_zero_off3_0(self,value):
        self.diff_dig_zero_off3_0_value = value 
        regvalue = self.diff_dig_zero_off3_0
        # perform operation with reg value 
            
    @property
    def diff_dig_idle_off11_8(self):
        self.diff_dig_idle_off11_8_pos   = 0
        self.diff_dig_idle_off11_8_len   = 4
        return self.diff_dig_idle_off11_8_value
        
    @diff_dig_idle_off11_8.setter
    def diff_dig_idle_off11_8(self,value):
        self.diff_dig_idle_off11_8_value = value 
        regvalue = self.diff_dig_idle_off11_8
        # perform operation with reg value 
             
class OTP_FIELDS_31 :
    
    def __init__(self) -> None:
        self.address = 0xcf
        self.page = 1
        
    @property
    def diff_dig_idle_off7_0(self):
        self.diff_dig_idle_off7_0_pos   = 0
        self.diff_dig_idle_off7_0_len   = 8
        return self.diff_dig_idle_off7_0_value
        
    @diff_dig_idle_off7_0.setter
    def diff_dig_idle_off7_0(self,value):
        self.diff_dig_idle_off7_0_value = value 
        regvalue = self.diff_dig_idle_off7_0
        # perform operation with reg value 
             
class OTP_FIELDS_32 :
    
    def __init__(self) -> None:
        self.address = 0xd0
        self.page = 1
        
    @property
    def int_ana_zero_off_gain011_4(self):
        self.int_ana_zero_off_gain011_4_pos   = 0
        self.int_ana_zero_off_gain011_4_len   = 8
        return self.int_ana_zero_off_gain011_4_value
        
    @int_ana_zero_off_gain011_4.setter
    def int_ana_zero_off_gain011_4(self,value):
        self.int_ana_zero_off_gain011_4_value = value 
        regvalue = self.int_ana_zero_off_gain011_4
        # perform operation with reg value 
             
class OTP_FIELDS_33 :
    
    def __init__(self) -> None:
        self.address = 0xd1
        self.page = 1
        
    @property
    def int_ana_zero_off_gain03_0(self):
        self.int_ana_zero_off_gain03_0_pos   = 4
        self.int_ana_zero_off_gain03_0_len   = 4
        return self.int_ana_zero_off_gain03_0_value
        
    @int_ana_zero_off_gain03_0.setter
    def int_ana_zero_off_gain03_0(self,value):
        self.int_ana_zero_off_gain03_0_value = value 
        regvalue = self.int_ana_zero_off_gain03_0
        # perform operation with reg value 
            
    @property
    def int_ana_idle_off_gain011_8(self):
        self.int_ana_idle_off_gain011_8_pos   = 0
        self.int_ana_idle_off_gain011_8_len   = 4
        return self.int_ana_idle_off_gain011_8_value
        
    @int_ana_idle_off_gain011_8.setter
    def int_ana_idle_off_gain011_8(self,value):
        self.int_ana_idle_off_gain011_8_value = value 
        regvalue = self.int_ana_idle_off_gain011_8
        # perform operation with reg value 
             
class OTP_FIELDS_34 :
    
    def __init__(self) -> None:
        self.address = 0xd2
        self.page = 1
        
    @property
    def int_ana_idle_off_gain07_0(self):
        self.int_ana_idle_off_gain07_0_pos   = 0
        self.int_ana_idle_off_gain07_0_len   = 8
        return self.int_ana_idle_off_gain07_0_value
        
    @int_ana_idle_off_gain07_0.setter
    def int_ana_idle_off_gain07_0(self,value):
        self.int_ana_idle_off_gain07_0_value = value 
        regvalue = self.int_ana_idle_off_gain07_0
        # perform operation with reg value 
             
class OTP_FIELDS_35 :
    
    def __init__(self) -> None:
        self.address = 0xd3
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain011_4(self):
        self.diff_ana_zero_off_gain011_4_pos   = 0
        self.diff_ana_zero_off_gain011_4_len   = 8
        return self.diff_ana_zero_off_gain011_4_value
        
    @diff_ana_zero_off_gain011_4.setter
    def diff_ana_zero_off_gain011_4(self,value):
        self.diff_ana_zero_off_gain011_4_value = value 
        regvalue = self.diff_ana_zero_off_gain011_4
        # perform operation with reg value 
             
class OTP_FIELDS_36 :
    
    def __init__(self) -> None:
        self.address = 0xd4
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain03_0(self):
        self.diff_ana_zero_off_gain03_0_pos   = 4
        self.diff_ana_zero_off_gain03_0_len   = 4
        return self.diff_ana_zero_off_gain03_0_value
        
    @diff_ana_zero_off_gain03_0.setter
    def diff_ana_zero_off_gain03_0(self,value):
        self.diff_ana_zero_off_gain03_0_value = value 
        regvalue = self.diff_ana_zero_off_gain03_0
        # perform operation with reg value 
            
    @property
    def diff_ana_idle_off_gain011_8(self):
        self.diff_ana_idle_off_gain011_8_pos   = 0
        self.diff_ana_idle_off_gain011_8_len   = 4
        return self.diff_ana_idle_off_gain011_8_value
        
    @diff_ana_idle_off_gain011_8.setter
    def diff_ana_idle_off_gain011_8(self,value):
        self.diff_ana_idle_off_gain011_8_value = value 
        regvalue = self.diff_ana_idle_off_gain011_8
        # perform operation with reg value 
             
class OTP_FIELDS_37 :
    
    def __init__(self) -> None:
        self.address = 0xd5
        self.page = 1
        
    @property
    def diff_ana_idle_off_gain07_0(self):
        self.diff_ana_idle_off_gain07_0_pos   = 0
        self.diff_ana_idle_off_gain07_0_len   = 8
        return self.diff_ana_idle_off_gain07_0_value
        
    @diff_ana_idle_off_gain07_0.setter
    def diff_ana_idle_off_gain07_0(self,value):
        self.diff_ana_idle_off_gain07_0_value = value 
        regvalue = self.diff_ana_idle_off_gain07_0
        # perform operation with reg value 
             
class OTP_FIELDS_38 :
    
    def __init__(self) -> None:
        self.address = 0xd6
        self.page = 1
        
    @property
    def int_ana_zero_off_gain111_4(self):
        self.int_ana_zero_off_gain111_4_pos   = 0
        self.int_ana_zero_off_gain111_4_len   = 8
        return self.int_ana_zero_off_gain111_4_value
        
    @int_ana_zero_off_gain111_4.setter
    def int_ana_zero_off_gain111_4(self,value):
        self.int_ana_zero_off_gain111_4_value = value 
        regvalue = self.int_ana_zero_off_gain111_4
        # perform operation with reg value 
             
class OTP_FIELDS_39 :
    
    def __init__(self) -> None:
        self.address = 0xd7
        self.page = 1
        
    @property
    def int_ana_zero_off_gain13_0(self):
        self.int_ana_zero_off_gain13_0_pos   = 4
        self.int_ana_zero_off_gain13_0_len   = 4
        return self.int_ana_zero_off_gain13_0_value
        
    @int_ana_zero_off_gain13_0.setter
    def int_ana_zero_off_gain13_0(self,value):
        self.int_ana_zero_off_gain13_0_value = value 
        regvalue = self.int_ana_zero_off_gain13_0
        # perform operation with reg value 
            
    @property
    def int_ana_idle_off_gain111_8(self):
        self.int_ana_idle_off_gain111_8_pos   = 0
        self.int_ana_idle_off_gain111_8_len   = 4
        return self.int_ana_idle_off_gain111_8_value
        
    @int_ana_idle_off_gain111_8.setter
    def int_ana_idle_off_gain111_8(self,value):
        self.int_ana_idle_off_gain111_8_value = value 
        regvalue = self.int_ana_idle_off_gain111_8
        # perform operation with reg value 
             
class OTP_FIELDS_40 :
    
    def __init__(self) -> None:
        self.address = 0xd8
        self.page = 1
        
    @property
    def int_ana_idle_off_gain17_0(self):
        self.int_ana_idle_off_gain17_0_pos   = 0
        self.int_ana_idle_off_gain17_0_len   = 8
        return self.int_ana_idle_off_gain17_0_value
        
    @int_ana_idle_off_gain17_0.setter
    def int_ana_idle_off_gain17_0(self,value):
        self.int_ana_idle_off_gain17_0_value = value 
        regvalue = self.int_ana_idle_off_gain17_0
        # perform operation with reg value 
             
class OTP_FIELDS_41 :
    
    def __init__(self) -> None:
        self.address = 0xd9
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain111_4(self):
        self.diff_ana_zero_off_gain111_4_pos   = 0
        self.diff_ana_zero_off_gain111_4_len   = 8
        return self.diff_ana_zero_off_gain111_4_value
        
    @diff_ana_zero_off_gain111_4.setter
    def diff_ana_zero_off_gain111_4(self,value):
        self.diff_ana_zero_off_gain111_4_value = value 
        regvalue = self.diff_ana_zero_off_gain111_4
        # perform operation with reg value 
             
class OTP_FIELDS_42 :
    
    def __init__(self) -> None:
        self.address = 0xda
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain13_0(self):
        self.diff_ana_zero_off_gain13_0_pos   = 4
        self.diff_ana_zero_off_gain13_0_len   = 4
        return self.diff_ana_zero_off_gain13_0_value
        
    @diff_ana_zero_off_gain13_0.setter
    def diff_ana_zero_off_gain13_0(self,value):
        self.diff_ana_zero_off_gain13_0_value = value 
        regvalue = self.diff_ana_zero_off_gain13_0
        # perform operation with reg value 
            
    @property
    def diff_ana_idle_off_gain111_8(self):
        self.diff_ana_idle_off_gain111_8_pos   = 0
        self.diff_ana_idle_off_gain111_8_len   = 4
        return self.diff_ana_idle_off_gain111_8_value
        
    @diff_ana_idle_off_gain111_8.setter
    def diff_ana_idle_off_gain111_8(self,value):
        self.diff_ana_idle_off_gain111_8_value = value 
        regvalue = self.diff_ana_idle_off_gain111_8
        # perform operation with reg value 
             
class OTP_FIELDS_43 :
    
    def __init__(self) -> None:
        self.address = 0xdb
        self.page = 1
        
    @property
    def diff_ana_idle_off_gain17_0(self):
        self.diff_ana_idle_off_gain17_0_pos   = 0
        self.diff_ana_idle_off_gain17_0_len   = 8
        return self.diff_ana_idle_off_gain17_0_value
        
    @diff_ana_idle_off_gain17_0.setter
    def diff_ana_idle_off_gain17_0(self,value):
        self.diff_ana_idle_off_gain17_0_value = value 
        regvalue = self.diff_ana_idle_off_gain17_0
        # perform operation with reg value 
             
class OTP_FIELDS_44 :
    
    def __init__(self) -> None:
        self.address = 0xdc
        self.page = 1
        
    @property
    def int_ana_zero_off_gain211_4(self):
        self.int_ana_zero_off_gain211_4_pos   = 0
        self.int_ana_zero_off_gain211_4_len   = 8
        return self.int_ana_zero_off_gain211_4_value
        
    @int_ana_zero_off_gain211_4.setter
    def int_ana_zero_off_gain211_4(self,value):
        self.int_ana_zero_off_gain211_4_value = value 
        regvalue = self.int_ana_zero_off_gain211_4
        # perform operation with reg value 
             
class OTP_FIELDS_45 :
    
    def __init__(self) -> None:
        self.address = 0xdd
        self.page = 1
        
    @property
    def int_ana_zero_off_gain23_0(self):
        self.int_ana_zero_off_gain23_0_pos   = 4
        self.int_ana_zero_off_gain23_0_len   = 4
        return self.int_ana_zero_off_gain23_0_value
        
    @int_ana_zero_off_gain23_0.setter
    def int_ana_zero_off_gain23_0(self,value):
        self.int_ana_zero_off_gain23_0_value = value 
        regvalue = self.int_ana_zero_off_gain23_0
        # perform operation with reg value 
            
    @property
    def int_ana_idle_off_gain211_8(self):
        self.int_ana_idle_off_gain211_8_pos   = 0
        self.int_ana_idle_off_gain211_8_len   = 4
        return self.int_ana_idle_off_gain211_8_value
        
    @int_ana_idle_off_gain211_8.setter
    def int_ana_idle_off_gain211_8(self,value):
        self.int_ana_idle_off_gain211_8_value = value 
        regvalue = self.int_ana_idle_off_gain211_8
        # perform operation with reg value 
             
class OTP_FIELDS_46 :
    
    def __init__(self) -> None:
        self.address = 0xde
        self.page = 1
        
    @property
    def int_ana_idle_off_gain27_0(self):
        self.int_ana_idle_off_gain27_0_pos   = 0
        self.int_ana_idle_off_gain27_0_len   = 8
        return self.int_ana_idle_off_gain27_0_value
        
    @int_ana_idle_off_gain27_0.setter
    def int_ana_idle_off_gain27_0(self,value):
        self.int_ana_idle_off_gain27_0_value = value 
        regvalue = self.int_ana_idle_off_gain27_0
        # perform operation with reg value 
             
class OTP_FIELDS_47 :
    
    def __init__(self) -> None:
        self.address = 0xdf
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain211_4(self):
        self.diff_ana_zero_off_gain211_4_pos   = 0
        self.diff_ana_zero_off_gain211_4_len   = 8
        return self.diff_ana_zero_off_gain211_4_value
        
    @diff_ana_zero_off_gain211_4.setter
    def diff_ana_zero_off_gain211_4(self,value):
        self.diff_ana_zero_off_gain211_4_value = value 
        regvalue = self.diff_ana_zero_off_gain211_4
        # perform operation with reg value 
             
class OTP_FIELDS_48 :
    
    def __init__(self) -> None:
        self.address = 0xe0
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain23_0(self):
        self.diff_ana_zero_off_gain23_0_pos   = 4
        self.diff_ana_zero_off_gain23_0_len   = 4
        return self.diff_ana_zero_off_gain23_0_value
        
    @diff_ana_zero_off_gain23_0.setter
    def diff_ana_zero_off_gain23_0(self,value):
        self.diff_ana_zero_off_gain23_0_value = value 
        regvalue = self.diff_ana_zero_off_gain23_0
        # perform operation with reg value 
            
    @property
    def diff_ana_idle_off_gain211_8(self):
        self.diff_ana_idle_off_gain211_8_pos   = 0
        self.diff_ana_idle_off_gain211_8_len   = 4
        return self.diff_ana_idle_off_gain211_8_value
        
    @diff_ana_idle_off_gain211_8.setter
    def diff_ana_idle_off_gain211_8(self,value):
        self.diff_ana_idle_off_gain211_8_value = value 
        regvalue = self.diff_ana_idle_off_gain211_8
        # perform operation with reg value 
             
class OTP_FIELDS_49 :
    
    def __init__(self) -> None:
        self.address = 0xe1
        self.page = 1
        
    @property
    def diff_ana_idle_off_gain27_0(self):
        self.diff_ana_idle_off_gain27_0_pos   = 0
        self.diff_ana_idle_off_gain27_0_len   = 8
        return self.diff_ana_idle_off_gain27_0_value
        
    @diff_ana_idle_off_gain27_0.setter
    def diff_ana_idle_off_gain27_0(self,value):
        self.diff_ana_idle_off_gain27_0_value = value 
        regvalue = self.diff_ana_idle_off_gain27_0
        # perform operation with reg value 
             
class OTP_FIELDS_50 :
    
    def __init__(self) -> None:
        self.address = 0xe2
        self.page = 1
        
    @property
    def int_ana_zero_off_gain311_4(self):
        self.int_ana_zero_off_gain311_4_pos   = 0
        self.int_ana_zero_off_gain311_4_len   = 8
        return self.int_ana_zero_off_gain311_4_value
        
    @int_ana_zero_off_gain311_4.setter
    def int_ana_zero_off_gain311_4(self,value):
        self.int_ana_zero_off_gain311_4_value = value 
        regvalue = self.int_ana_zero_off_gain311_4
        # perform operation with reg value 
             
class OTP_FIELDS_51 :
    
    def __init__(self) -> None:
        self.address = 0xe3
        self.page = 1
        
    @property
    def int_ana_zero_off_gain33_0(self):
        self.int_ana_zero_off_gain33_0_pos   = 4
        self.int_ana_zero_off_gain33_0_len   = 4
        return self.int_ana_zero_off_gain33_0_value
        
    @int_ana_zero_off_gain33_0.setter
    def int_ana_zero_off_gain33_0(self,value):
        self.int_ana_zero_off_gain33_0_value = value 
        regvalue = self.int_ana_zero_off_gain33_0
        # perform operation with reg value 
            
    @property
    def int_ana_idle_off_gain311_8(self):
        self.int_ana_idle_off_gain311_8_pos   = 0
        self.int_ana_idle_off_gain311_8_len   = 4
        return self.int_ana_idle_off_gain311_8_value
        
    @int_ana_idle_off_gain311_8.setter
    def int_ana_idle_off_gain311_8(self,value):
        self.int_ana_idle_off_gain311_8_value = value 
        regvalue = self.int_ana_idle_off_gain311_8
        # perform operation with reg value 
             
class OTP_FIELDS_52 :
    
    def __init__(self) -> None:
        self.address = 0xe4
        self.page = 1
        
    @property
    def int_ana_idle_off_gain37_0(self):
        self.int_ana_idle_off_gain37_0_pos   = 0
        self.int_ana_idle_off_gain37_0_len   = 8
        return self.int_ana_idle_off_gain37_0_value
        
    @int_ana_idle_off_gain37_0.setter
    def int_ana_idle_off_gain37_0(self,value):
        self.int_ana_idle_off_gain37_0_value = value 
        regvalue = self.int_ana_idle_off_gain37_0
        # perform operation with reg value 
             
class OTP_FIELDS_53 :
    
    def __init__(self) -> None:
        self.address = 0xe5
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain311_4(self):
        self.diff_ana_zero_off_gain311_4_pos   = 0
        self.diff_ana_zero_off_gain311_4_len   = 8
        return self.diff_ana_zero_off_gain311_4_value
        
    @diff_ana_zero_off_gain311_4.setter
    def diff_ana_zero_off_gain311_4(self,value):
        self.diff_ana_zero_off_gain311_4_value = value 
        regvalue = self.diff_ana_zero_off_gain311_4
        # perform operation with reg value 
             
class OTP_FIELDS_54 :
    
    def __init__(self) -> None:
        self.address = 0xe6
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain33_0(self):
        self.diff_ana_zero_off_gain33_0_pos   = 4
        self.diff_ana_zero_off_gain33_0_len   = 4
        return self.diff_ana_zero_off_gain33_0_value
        
    @diff_ana_zero_off_gain33_0.setter
    def diff_ana_zero_off_gain33_0(self,value):
        self.diff_ana_zero_off_gain33_0_value = value 
        regvalue = self.diff_ana_zero_off_gain33_0
        # perform operation with reg value 
            
    @property
    def diff_ana_idle_off_gain311_8(self):
        self.diff_ana_idle_off_gain311_8_pos   = 0
        self.diff_ana_idle_off_gain311_8_len   = 4
        return self.diff_ana_idle_off_gain311_8_value
        
    @diff_ana_idle_off_gain311_8.setter
    def diff_ana_idle_off_gain311_8(self,value):
        self.diff_ana_idle_off_gain311_8_value = value 
        regvalue = self.diff_ana_idle_off_gain311_8
        # perform operation with reg value 
             
class OTP_FIELDS_55 :
    
    def __init__(self) -> None:
        self.address = 0xe7
        self.page = 1
        
    @property
    def diff_ana_idle_off_gain37_0(self):
        self.diff_ana_idle_off_gain37_0_pos   = 0
        self.diff_ana_idle_off_gain37_0_len   = 8
        return self.diff_ana_idle_off_gain37_0_value
        
    @diff_ana_idle_off_gain37_0.setter
    def diff_ana_idle_off_gain37_0(self,value):
        self.diff_ana_idle_off_gain37_0_value = value 
        regvalue = self.diff_ana_idle_off_gain37_0
        # perform operation with reg value 
             
class OTP_FIELDS_56 :
    
    def __init__(self) -> None:
        self.address = 0xe8
        self.page = 1
        
    @property
    def int_ana_zero_off_gain411_4(self):
        self.int_ana_zero_off_gain411_4_pos   = 0
        self.int_ana_zero_off_gain411_4_len   = 8
        return self.int_ana_zero_off_gain411_4_value
        
    @int_ana_zero_off_gain411_4.setter
    def int_ana_zero_off_gain411_4(self,value):
        self.int_ana_zero_off_gain411_4_value = value 
        regvalue = self.int_ana_zero_off_gain411_4
        # perform operation with reg value 
             
class OTP_FIELDS_57 :
    
    def __init__(self) -> None:
        self.address = 0xe9
        self.page = 1
        
    @property
    def int_ana_zero_off_gain43_0(self):
        self.int_ana_zero_off_gain43_0_pos   = 4
        self.int_ana_zero_off_gain43_0_len   = 4
        return self.int_ana_zero_off_gain43_0_value
        
    @int_ana_zero_off_gain43_0.setter
    def int_ana_zero_off_gain43_0(self,value):
        self.int_ana_zero_off_gain43_0_value = value 
        regvalue = self.int_ana_zero_off_gain43_0
        # perform operation with reg value 
            
    @property
    def int_ana_idle_off_gain411_8(self):
        self.int_ana_idle_off_gain411_8_pos   = 0
        self.int_ana_idle_off_gain411_8_len   = 4
        return self.int_ana_idle_off_gain411_8_value
        
    @int_ana_idle_off_gain411_8.setter
    def int_ana_idle_off_gain411_8(self,value):
        self.int_ana_idle_off_gain411_8_value = value 
        regvalue = self.int_ana_idle_off_gain411_8
        # perform operation with reg value 
             
class OTP_FIELDS_58 :
    
    def __init__(self) -> None:
        self.address = 0xea
        self.page = 1
        
    @property
    def int_ana_idle_off_gain47_0(self):
        self.int_ana_idle_off_gain47_0_pos   = 0
        self.int_ana_idle_off_gain47_0_len   = 8
        return self.int_ana_idle_off_gain47_0_value
        
    @int_ana_idle_off_gain47_0.setter
    def int_ana_idle_off_gain47_0(self,value):
        self.int_ana_idle_off_gain47_0_value = value 
        regvalue = self.int_ana_idle_off_gain47_0
        # perform operation with reg value 
             
class OTP_FIELDS_59 :
    
    def __init__(self) -> None:
        self.address = 0xeb
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain411_4(self):
        self.diff_ana_zero_off_gain411_4_pos   = 0
        self.diff_ana_zero_off_gain411_4_len   = 8
        return self.diff_ana_zero_off_gain411_4_value
        
    @diff_ana_zero_off_gain411_4.setter
    def diff_ana_zero_off_gain411_4(self,value):
        self.diff_ana_zero_off_gain411_4_value = value 
        regvalue = self.diff_ana_zero_off_gain411_4
        # perform operation with reg value 
             
class OTP_FIELDS_60 :
    
    def __init__(self) -> None:
        self.address = 0xec
        self.page = 1
        
    @property
    def diff_ana_zero_off_gain43_0(self):
        self.diff_ana_zero_off_gain43_0_pos   = 4
        self.diff_ana_zero_off_gain43_0_len   = 4
        return self.diff_ana_zero_off_gain43_0_value
        
    @diff_ana_zero_off_gain43_0.setter
    def diff_ana_zero_off_gain43_0(self,value):
        self.diff_ana_zero_off_gain43_0_value = value 
        regvalue = self.diff_ana_zero_off_gain43_0
        # perform operation with reg value 
            
    @property
    def diff_ana_idle_off_gain411_8(self):
        self.diff_ana_idle_off_gain411_8_pos   = 0
        self.diff_ana_idle_off_gain411_8_len   = 4
        return self.diff_ana_idle_off_gain411_8_value
        
    @diff_ana_idle_off_gain411_8.setter
    def diff_ana_idle_off_gain411_8(self,value):
        self.diff_ana_idle_off_gain411_8_value = value 
        regvalue = self.diff_ana_idle_off_gain411_8
        # perform operation with reg value 
             
class OTP_FIELDS_61 :
    
    def __init__(self) -> None:
        self.address = 0xed
        self.page = 1
        
    @property
    def diff_ana_idle_off_gain47_0(self):
        self.diff_ana_idle_off_gain47_0_pos   = 0
        self.diff_ana_idle_off_gain47_0_len   = 8
        return self.diff_ana_idle_off_gain47_0_value
        
    @diff_ana_idle_off_gain47_0.setter
    def diff_ana_idle_off_gain47_0(self,value):
        self.diff_ana_idle_off_gain47_0_value = value 
        regvalue = self.diff_ana_idle_off_gain47_0
        # perform operation with reg value 
             
class OTP_FIELDS_62 :
    
    def __init__(self) -> None:
        self.address = 0xee
        self.page = 1
        
    @property
    def spare12_0(self):
        self.spare12_0_pos   = 5
        self.spare12_0_len   = 3
        return self.spare12_0_value
        
    @spare12_0.setter
    def spare12_0(self,value):
        self.spare12_0_value = value 
        regvalue = self.spare12_0
        # perform operation with reg value 
            
    @property
    def auto_mode_retry_en(self):
        self.auto_mode_retry_en_pos   = 4
        self.auto_mode_retry_en_len   = 1
        return self.auto_mode_retry_en_value
        
    @auto_mode_retry_en.setter
    def auto_mode_retry_en(self,value):
        self.auto_mode_retry_en_value = value 
        regvalue = self.auto_mode_retry_en
        # perform operation with reg value 
            
    @property
    def auto_mode_i2c_dis(self):
        self.auto_mode_i2c_dis_pos   = 3
        self.auto_mode_i2c_dis_len   = 1
        return self.auto_mode_i2c_dis_value
        
    @auto_mode_i2c_dis.setter
    def auto_mode_i2c_dis(self,value):
        self.auto_mode_i2c_dis_value = value 
        regvalue = self.auto_mode_i2c_dis
        # perform operation with reg value 
            
    @property
    def auto_mode_fault_en(self):
        self.auto_mode_fault_en_pos   = 2
        self.auto_mode_fault_en_len   = 1
        return self.auto_mode_fault_en_value
        
    @auto_mode_fault_en.setter
    def auto_mode_fault_en(self,value):
        self.auto_mode_fault_en_value = value 
        regvalue = self.auto_mode_fault_en
        # perform operation with reg value 
            
    @property
    def platf_ref_dvddldo_mode(self):
        self.platf_ref_dvddldo_mode_pos   = 1
        self.platf_ref_dvddldo_mode_len   = 1
        return self.platf_ref_dvddldo_mode_value
        
    @platf_ref_dvddldo_mode.setter
    def platf_ref_dvddldo_mode(self,value):
        self.platf_ref_dvddldo_mode_value = value 
        regvalue = self.platf_ref_dvddldo_mode
        # perform operation with reg value 
            
    @property
    def auto_mode_dis(self):
        self.auto_mode_dis_pos   = 0
        self.auto_mode_dis_len   = 1
        return self.auto_mode_dis_value
        
    @auto_mode_dis.setter
    def auto_mode_dis(self,value):
        self.auto_mode_dis_value = value 
        regvalue = self.auto_mode_dis
        # perform operation with reg value 
             
class OTP_FIELDS_63 :
    
    def __init__(self) -> None:
        self.address = 0xef
        self.page = 1
        
    @property
    def otp_fro_sel_0p8125mhz(self):
        self.otp_fro_sel_0p8125mhz_pos   = 7
        self.otp_fro_sel_0p8125mhz_len   = 1
        return self.otp_fro_sel_0p8125mhz_value
        
    @otp_fro_sel_0p8125mhz.setter
    def otp_fro_sel_0p8125mhz(self,value):
        self.otp_fro_sel_0p8125mhz_value = value 
        regvalue = self.otp_fro_sel_0p8125mhz
        # perform operation with reg value 
            
    @property
    def otp_fro_sel_1p625mhz(self):
        self.otp_fro_sel_1p625mhz_pos   = 6
        self.otp_fro_sel_1p625mhz_len   = 1
        return self.otp_fro_sel_1p625mhz_value
        
    @otp_fro_sel_1p625mhz.setter
    def otp_fro_sel_1p625mhz(self,value):
        self.otp_fro_sel_1p625mhz_value = value 
        regvalue = self.otp_fro_sel_1p625mhz
        # perform operation with reg value 
            
    @property
    def otp_fro_sel(self):
        self.otp_fro_sel_pos   = 5
        self.otp_fro_sel_len   = 1
        return self.otp_fro_sel_value
        
    @otp_fro_sel.setter
    def otp_fro_sel(self,value):
        self.otp_fro_sel_value = value 
        regvalue = self.otp_fro_sel
        # perform operation with reg value 
            
    @property
    def fro_freq_adj4_0(self):
        self.fro_freq_adj4_0_pos   = 0
        self.fro_freq_adj4_0_len   = 5
        return self.fro_freq_adj4_0_value
        
    @fro_freq_adj4_0.setter
    def fro_freq_adj4_0(self,value):
        self.fro_freq_adj4_0_value = value 
        regvalue = self.fro_freq_adj4_0
        # perform operation with reg value 
            