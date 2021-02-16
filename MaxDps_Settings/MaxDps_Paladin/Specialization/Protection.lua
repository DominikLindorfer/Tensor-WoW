local _, addonTable = ...;

--- @type MaxDps
if not MaxDps then
	return
end

local Paladin = addonTable.Paladin;
local MaxDps = MaxDps;
local GetTotemInfo = GetTotemInfo;

local PR = {
	AvengingWrath            = 31884,
	Seraphim                 = 152262,
	ShieldOfTheRighteous     = 53600,
	ShieldOfTheRighteousAura = 132403,
	Consecration             = 26573,
	Judgment                 = 275779,
	CrusadersJudgment        = 204023,
	AvengersShield           = 31935,
	AvengersValor            = 197561,
	BlessedHammer            = 204019,
	BastionOfLight           = 204035,
	HammerOfTheRighteous     = 53595,
	HammerOfWrath            = 24275,
	WordOfGlory              = 85673,
	ArdentDefender = 31850,
	DivineToll = 304971,
	GuardianOfAncientKings = 86659,
	ShiningLight = 327510,
};

setmetatable(PR, Paladin.spellMeta);

function Paladin:Protection()
	local fd = MaxDps.FrameData;
	local cooldown = fd.cooldown;
	local buff = fd.buff;
	local talents = fd.talents;
	local gcd = fd.gcd;
	local targetHp = MaxDps:TargetPercentHealth() * 100;
	local consecrationUp = GetTotemInfo(1);
	
	local health = UnitHealth('player');
	local healthMax = UnitHealthMax('player');
	local healthPercent = (health / healthMax) * 100;
	local holyPower = UnitPower('player', HolyPower);
	
	-- Essences
	MaxDps:GlowEssences();
	
	-- Cooldowns
	
	if healthPercent <= 50 then
		MaxDps:GlowCooldown(PR.ArdentDefender, cooldown[PR.ArdentDefender].ready);
	end
	
	if healthPercent <= 30 then
		MaxDps:GlowCooldown(PR.GuardianOfAncientKings, cooldown[PR.GuardianOfAncientKings].ready);
	end
	
	if buff[PR.ShiningLight].up and healthPercent <= 75 then
		MaxDps:GlowCooldown(PR.WordOfGlory, cooldown[PR.WordOfGlory].ready);
	end
	
	if healthPercent <= 65 and holyPower > 2 then
		MaxDps:GlowCooldown(PR.WordOfGlory, cooldown[PR.WordOfGlory].ready);
	end
	
	MaxDps:GlowCooldown(PR.AvengingWrath, cooldown[PR.AvengingWrath].ready);

	if talents[PR.Seraphim] then
		MaxDps:GlowCooldown(PR.Seraphim, cooldown[PR.Seraphim].ready);
	end
		
	if holyPower > 2 then
		MaxDps:GlowCooldown(PR.ShieldOfTheRighteous, not buff[PR.ShieldOfTheRighteousAura].up);
	end
	
	if holyPower > 4 then
		MaxDps:GlowCooldown(PR.ShieldOfTheRighteous, cooldown[PR.ShieldOfTheRighteous].ready);
	end
		
	--Paladin:ProtectionCooldowns();
		
	if cooldown[PR.Consecration].ready and (not consecrationUp) then
		return PR.Consecration;
	end
	
	--if cooldown[PR.DivineToll].ready then
		--return PR.DivineToll;
	--end
	
	if cooldown[PR.Judgment].ready then
		return PR.Judgment;
	end

	if cooldown[PR.HammerOfWrath].ready and targetHp <= 20 then
		return PR.HammerOfWrath;
	end

	if cooldown[PR.AvengersShield].ready then
		return PR.AvengersShield;
	end

	if talents[PR.BlessedHammer] and cooldown[PR.BlessedHammer].ready then
		return PR.BlessedHammer;
	end

	if cooldown[PR.HammerOfTheRighteous].ready then
		return PR.HammerOfTheRighteous;
	end

	if cooldown[PR.Consecration].ready then
		return PR.Consecration;
	end
end

function Paladin:ProtectionCooldowns()
	local fd = MaxDps.FrameData;
	local cooldown = fd.cooldown;
	local buff = fd.buff;
	local talents = fd.talents;
	local health = UnitHealth('player');
	local healthMax = UnitHealthMax('player');
	local healthPercent = (health / healthMax) * 100;
	local holyPower = UnitPower('player', 9);
	MaxDps:GlowEssences();

	if not buff[PR.ShieldOfTheRighteousAura].up and holyPower == 5 then
		MaxDps:GlowCooldown(PR.ShieldOfTheRighteous);
	end

	if healthPercent <= 70 and holyPower > 2 then
		MaxDps:GlowCooldown(PR.WordOfGlory);
	end

	MaxDps:GlowCooldown(PR.AvengingWrath, cooldown[PR.AvengingWrath].ready);

	if talents[PR.Seraphim] then
		MaxDps:GlowCooldown(PR.Seraphim, cooldown[PR.Seraphim].ready);
	end

	if talents[PR.BastionOfLight] then
		MaxDps:GlowCooldown(PR.BastionOfLight, cooldown[PR.BastionOfLight].ready and (cooldown[PR.ShieldOfTheRighteous].charges <= 0.5));
	end
end
