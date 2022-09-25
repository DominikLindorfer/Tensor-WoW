local _, addonTable = ...;

--- @type MaxDps
if not MaxDps then
	return
end

local Warrior = addonTable.Warrior;
local MaxDps = MaxDps;
local UnitPower = UnitPower;
local UnitHealth = UnitHealth;
local UnitAura = UnitAura;
local GetSpellDescription = GetSpellDescription;
local UnitHealthMax = UnitHealthMax;
local UnitPowerMax = UnitPowerMax;
local PowerTypeRage = Enum.PowerType.Rage;

local PR = {
	Avatar            = 107574,
	ThunderClap       = 6343,
	UnstoppableForce  = 275336,
	ShieldBlock       = 2565,
	ShieldBlockAura   = 132404,
	ShieldSlam        = 23922,
	LastStand         = 12975,
	Bolster           = 280001,
	IgnorePain        = 190456,
	BoomingVoice      = 202743,
	DemoralizingShout = 1160,
	Ravager           = 228920,
	DragonRoar        = 118000,
	Revenge           = 6572,
	NeverSurrender    = 202561,
	RevengeAura       = 5302,
	Devastate         = 20243,
	ImpendingVictory = 202168,
	Battleshout = 6673,
	Shockwave = 46968,
	Shieldwall = 871,
	Execute = 163201,
	Whirlwind = 1680,
};

setmetatable(PR, Warrior.spellMeta);

function Warrior:Protection()
	local fd = MaxDps.FrameData;
	local cooldown = fd.cooldown;
	local buff = fd.buff;
	local talents = fd.talents;
	local rage = UnitPower('player', PowerTypeRage);
	local rageMax = UnitPowerMax('player', PowerTypeRage);
	local rageDeficit = rageMax - rage;
	local curentHP = UnitHealth('player');
	local maxHP = UnitHealthMax('player');
	local healthPerc = (curentHP / maxHP) * 100;
	MaxDps:GlowEssences();
	
	if healthPerc <= 40 then
		return MaxDps:GlowCooldown(PR.Shieldwall, cooldown[PR.Shieldwall].ready);
	end
	
	if healthPerc <= 45 then
		return MaxDps:GlowCooldown(PR.LastStand, cooldown[PR.LastStand].ready);
	end
	
	if healthPerc <= 65 and rage >= 10 then
		return MaxDps:GlowCooldown(PR.ImpendingVictory, cooldown[PR.ImpendingVictory].ready);
	end
	
	MaxDps:GlowCooldown(PR.Avatar, cooldown[PR.Avatar].ready);
	
	if talents[PR.DragonRoar] and cooldown[PR.DragonRoar].ready then
		return PR.DragonRoar;
	end
	
	if cooldown[PR.Revenge].ready and buff[PR.RevengeAura].up then
		return PR.Revenge;
	end
	
	if cooldown[PR.DemoralizingShout].ready then
		return PR.DemoralizingShout;
	end
	
	if buff[PR.IgnorePain].refreshable and rage >= 40 then
		MaxDps:GlowCooldown(PR.IgnorePain, cooldown[PR.IgnorePain].ready);
	end
	
	if cooldown[PR.ShieldBlock].ready and not buff[PR.ShieldBlockAura].up then
		MaxDps:GlowCooldown(PR.ShieldBlock, cooldown[PR.ShieldBlock].ready);
	end
	
	if cooldown[PR.Ravager].ready then
		return PR.Ravager
	end
	
	if cooldown[PR.Shockwave].ready then
		MaxDps:GlowCooldown(PR.Shockwave, cooldown[PR.Shockwave].ready);
	end
	
	-- thunder_clap,if=(talent.unstoppable_force.enabled&buff.avatar.up);
	if cooldown[PR.ThunderClap].ready then
		return PR.ThunderClap;
	end
	
	if cooldown[PR.ShieldSlam].ready then
		return PR.ShieldSlam;
	end	

	if cooldown[PR.Revenge].ready and rage > 55 then
		return PR.Revenge;
	end
	
	if cooldown[PR.Devastate].ready then
		return PR.Devastate;
	end

end