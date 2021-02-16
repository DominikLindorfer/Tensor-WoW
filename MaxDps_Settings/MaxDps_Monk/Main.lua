local addonName, addonTable = ...;
_G[addonName] = addonTable;

--- @type MaxDps
if not MaxDps then return end

local MaxDps = MaxDps;
local Monk = MaxDps:NewModule('Monk');
addonTable.Monk = Monk;

-- Auras
local _HitComboAura = 196741;
local _BlackoutKickAura = 116768;
local _RushingJadeWindAura = 148187;

Monk.spellMeta = {
	__index = function(t, k)
		print('Spell Key ' .. k .. ' not found!');
	end
}

function Monk:Enable()
	if MaxDps.Spec == 1 then
		MaxDps.NextSpell = Monk.Brewmaster;
		MaxDps:Print(MaxDps.Colors.Info .. 'Monk Brewmaster');
	elseif MaxDps.Spec == 2 then
		MaxDps.NextSpell = Monk.Mistweaver;
		MaxDps:Print(MaxDps.Colors.Info .. 'Monk Mistweaver');
	elseif MaxDps.Spec == 3 then
		MaxDps.NextSpell = Monk.Windwalker;
		MaxDps:Print(MaxDps.Colors.Info .. 'Monk Windwalker');
	end

	return true;
end